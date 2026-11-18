#!/usr/bin/env python3
"""Validate common Seedance 2.5 prompt contracts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


EPSILON = 1e-6

SECOND_RANGE_RE = re.compile(
    r"(?P<start>\d+(?:\.\d+)?)\s*(?:—|–|-|~|至)\s*"
    r"(?P<end>\d+(?:\.\d+)?)\s*(?:秒|s)",
    re.IGNORECASE,
)
CLOCK_RANGE_RE = re.compile(
    r"\[?\s*(?P<start_min>\d{1,2}):(?P<start_sec>\d{2}(?:\.\d+)?)\s*"
    r"(?:—|–|-)\s*(?P<end_min>\d{1,2}):(?P<end_sec>\d{2}(?:\.\d+)?)\s*"
    r"(?:s)?\s*\]?",
    re.IGNORECASE,
)
TIME_TITLE_RE = re.compile(
    r"(?:\d+(?:\.\d+)?\s*(?:—|–|-|~|至)\s*\d+(?:\.\d+)?\s*(?:秒|s)"
    r"|\[\s*\d{1,2}:\d{2}(?:\.\d+)?\s*(?:—|–|-)\s*"
    r"\d{1,2}:\d{2}(?:\.\d+)?\s*(?:s)?\s*\])\s*【[^】\r\n]+】",
    re.IGNORECASE,
)
UI_PARAMETER_PATTERNS = (
    re.compile(r"(?:全片|总时长|视频时长)\s*[:：]?\s*\d+(?:\.\d+)?\s*秒", re.IGNORECASE),
    re.compile(r"(?<!\d)(?:16\s*[:：]\s*9|9\s*[:：]\s*16|21\s*[:：]\s*9)(?!\d)"),
    re.compile(r"(?<!\d)(?:480|720|1080)\s*p\+?(?!\w)", re.IGNORECASE),
)
NEGATIVE_PHRASE_RE = re.compile(
    r"不要|没有|不是|禁止|避免|不参考|不出现|不切换|不融合|不互换"
    r"|无(?!缝|论|数|限|人机|线|比)"
)
AUDIO_REFERENCE_RE = re.compile(r"@音频\s*(\d+)")
DIALOGUE_RE = re.compile(r"「[^」]+」")
VOICE_BINDING_RE = re.compile(r"声音参考|音色|@音频\s*\d+")
RISKY_WORDS = {
    "逆光": "“逆光”会在角色头顶生成光晕，改写光源在画外哪一侧。",
    "大声": "“大声”会把音高抬离声音参考，语气写平常的。",
}
WHITE_MODEL_DIMENSION_RE = re.compile(
    r"(?:参考|保留|保持)[^。；\n]{0,100}"
    r"(?:运镜|动作|动线|运动轨迹|角色站位|站位|光影变化|镜头切接|构图|画面节奏)"
)
WHITE_MODEL_MAPPING_RE = re.compile(
    r"(?:模型|人物|角色|主体)[^。；\n]{0,80}(?:对应|替换为|映射为|代表)"
    r"|(?:对应|替换为|映射为|代表)[^。；\n]{0,80}(?:@?图(?:片)?\s*\d+|角色|人物|主体)"
)


@dataclass(frozen=True)
class Issue:
    level: str
    code: str
    message: str


@dataclass(frozen=True)
class TimeRange:
    start: float
    end: float
    offset: int


def _time_ranges(text: str) -> list[TimeRange]:
    ranges: list[TimeRange] = []
    for match in SECOND_RANGE_RE.finditer(text):
        ranges.append(TimeRange(float(match.group("start")), float(match.group("end")), match.start()))
    for match in CLOCK_RANGE_RE.finditer(text):
        start = int(match.group("start_min")) * 60 + float(match.group("start_sec"))
        end = int(match.group("end_min")) * 60 + float(match.group("end_sec"))
        ranges.append(TimeRange(start, end, match.start()))
    return sorted(ranges, key=lambda item: item.offset)


def _segments(text: str) -> list[str]:
    ranges = _time_ranges(text)
    bounds = [item.offset for item in ranges] + [len(text)]
    return [text[start:end] for start, end in zip(bounds, bounds[1:])]


def _timestamp_issues(ranges: list[TimeRange], duration: float | None) -> list[Issue]:
    if not ranges:
        return []

    issues: list[Issue] = []
    if abs(ranges[0].start) > EPSILON:
        issues.append(Issue("ERROR", "timestamp-start", "时间轴必须从 0 秒开始。"))

    for previous, current in zip(ranges, ranges[1:]):
        if current.start > previous.end + EPSILON:
            issues.append(Issue("ERROR", "timestamp-gap", "相邻时间段之间存在空隙。"))
        elif current.start < previous.end - EPSILON:
            issues.append(Issue("ERROR", "timestamp-overlap", "相邻时间段发生重叠。"))

    if duration is not None and abs(ranges[-1].end - duration) > EPSILON:
        issues.append(
            Issue("ERROR", "timestamp-end", f"最后时间戳应在 {duration:g} 秒结束。")
        )
    return issues


def validate_prompt(
    text: str,
    duration: float | None = None,
    mode: str = "auto",
) -> list[Issue]:
    """Return deterministic prompt issues in document order."""
    issues: list[Issue] = []

    if any(pattern.search(text) for pattern in UI_PARAMETER_PATTERNS):
        issues.append(
            Issue("ERROR", "ui-parameter", "时长、画幅比例和分辨率应在即梦界面设置。")
        )
    if TIME_TITLE_RE.search(text):
        issues.append(Issue("ERROR", "time-title", "时间后只写冒号，不添加【小标题】。"))

    issues.extend(_timestamp_issues(_time_ranges(text), duration))

    audio_refs = set(AUDIO_REFERENCE_RE.findall(text))
    if len(audio_refs) > 2:
        issues.append(
            Issue(
                "WARN",
                "voice-reference-count",
                f"一条绑了 {len(audio_refs)} 条声音参考，超过两条时音色容易串到别的角色身上；拆成两条，每条两人说话。",
            )
        )

    for segment in _segments(text):
        if DIALOGUE_RE.search(segment) and not VOICE_BINDING_RE.search(segment):
            issues.append(
                Issue(
                    "WARN",
                    "dialogue-voice-binding",
                    f"这一段的台词没有点名声音参考：{segment[:24]}……",
                )
            )

    for word, message in RISKY_WORDS.items():
        if word in text:
            issues.append(Issue("WARN", "risky-word", message))

    negative_phrases = sorted(set(NEGATIVE_PHRASE_RE.findall(text)))
    if negative_phrases:
        issues.append(
            Issue(
                "WARN",
                "negative-phrasing",
                f"改写成正面描述，写画面里有什么：{'、'.join(negative_phrases)}。",
            )
        )

    is_white_model = mode == "white-model" or "白模" in text
    if is_white_model and not WHITE_MODEL_DIMENSION_RE.search(text):
        issues.append(
            Issue(
                "ERROR",
                "white-model-reference",
                "白模提示词必须明确要参考的运镜、动作、动线、站位或其他动态维度。",
            )
        )

    has_character_replacement = bool(re.search(r"白模[^。；\n]{0,80}(?:人物|角色|主体)", text))
    if is_white_model and has_character_replacement and not WHITE_MODEL_MAPPING_RE.search(text):
        issues.append(
            Issue(
                "ERROR",
                "white-model-mapping",
                "替换白模人物时必须写明模型与角色或参考图的对应关系。",
            )
        )

    return issues


def _read_prompt(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8-sig")


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="校验 Seedance 2.5 视频提示词")
    parser.add_argument("prompt", help="UTF-8 提示词文件；使用 - 从标准输入读取")
    parser.add_argument("--duration", type=float, help="即梦界面设置的目标时长（秒）")
    parser.add_argument(
        "--mode",
        choices=("auto", "standard", "white-model", "edit", "extend", "long"),
        default="auto",
    )
    parser.add_argument("--json", action="store_true", help="以 JSON 输出检查结果")
    args = parser.parse_args(argv)

    issues = validate_prompt(_read_prompt(args.prompt), duration=args.duration, mode=args.mode)
    if args.json:
        print(json.dumps([asdict(issue) for issue in issues], ensure_ascii=False, indent=2))
    elif issues:
        for issue in issues:
            print(f"[{issue.level}] {issue.code}: {issue.message}")
    else:
        print("PASS")

    return 1 if any(issue.level == "ERROR" for issue in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
