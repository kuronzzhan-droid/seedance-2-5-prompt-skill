import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_prompt import validate_prompt


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_prompt.py"


def issue_codes(text: str, *, duration: float | None = None, mode: str = "auto") -> set[str]:
    return {issue.code for issue in validate_prompt(text, duration=duration, mode=mode)}


class ValidatePromptTests(unittest.TestCase):
    def test_rejects_ui_parameters_and_time_titles(self) -> None:
        prompt = "全片30秒，16:9，720P。\n0—5秒【开场】：角色走近。\n5—30秒：角色离开。"

        codes = issue_codes(prompt, duration=30)

        self.assertIn("ui-parameter", codes)
        self.assertIn("time-title", codes)

    def test_accepts_continuous_unequal_ranges(self) -> None:
        prompt = "0—4秒：角色走近。\n4—9秒：角色说话。\n9—30秒：角色离开。"

        issues = validate_prompt(prompt, duration=30)

        self.assertEqual([], issues)

    def test_rejects_timestamp_gap(self) -> None:
        prompt = "0—4秒：角色走近。\n5—10秒：角色说话。"

        codes = issue_codes(prompt, duration=10)

        self.assertIn("timestamp-gap", codes)

    def test_rejects_timestamp_overlap(self) -> None:
        prompt = "0—6秒：角色走近。\n5—10秒：角色说话。"

        codes = issue_codes(prompt, duration=10)

        self.assertIn("timestamp-overlap", codes)

    def test_rejects_wrong_timestamp_end(self) -> None:
        prompt = "0—4秒：角色走近。\n4—9秒：角色说话。"

        codes = issue_codes(prompt, duration=10)

        self.assertIn("timestamp-end", codes)

    def test_white_model_requires_reference_dimensions_and_mapping(self) -> None:
        prompt = "参考@视频1的白模人物，生成最终角色画面。"

        codes = issue_codes(prompt, mode="white-model")

        self.assertIn("white-model-reference", codes)
        self.assertIn("white-model-mapping", codes)

    def test_accepts_explicit_white_model_reference_and_mapping(self) -> None:
        prompt = (
            "只参考@视频1的运镜、动作、动线和角色站位，外观以@图1和@图2为准。"
            "@视频1中的右侧模型对应@图1的角色甲，左侧模型对应@图2的角色乙。"
        )

        issues = validate_prompt(prompt, mode="white-model")

        self.assertEqual([], issues)

    def test_rejects_wide_aspect_ratio_in_prompt(self) -> None:
        codes = issue_codes("21:9，三渲二。\n0—30秒：角色走近。", duration=30)

        self.assertIn("ui-parameter", codes)

    def test_warns_on_negative_phrasing(self) -> None:
        issues = validate_prompt("0—30秒：画面里不要出现路人，无字幕。", duration=30)

        self.assertEqual(["negative-phrasing"], [issue.code for issue in issues])
        self.assertEqual("WARN", issues[0].level)
        self.assertIn("不要", issues[0].message)
        self.assertIn("无", issues[0].message)

    def test_allows_words_that_merely_contain_wu(self) -> None:
        prompt = "0—30秒：两段画面无缝衔接，镜头跟着无人机升高。"

        self.assertEqual([], validate_prompt(prompt, duration=30))

    def test_accepts_positive_phrasing(self) -> None:
        prompt = "0—30秒：画面里只有马格努斯，全段是环境声和动作声。"

        self.assertEqual([], validate_prompt(prompt, duration=30))

    def test_warns_on_more_than_two_voice_references(self) -> None:
        prompt = "@音频1 甲。@音频2 乙。@音频3 丙。\n0—30秒：三人坐在桌边。"

        self.assertIn("voice-reference-count", issue_codes(prompt, duration=30))

    def test_warns_on_dialogue_without_voice_reference(self) -> None:
        prompt = "0—4秒：白说：「来了。」\n4—30秒：用白的声音参考的音色说：「走吧。」"

        issues = validate_prompt(prompt, duration=30)

        self.assertEqual(["dialogue-voice-binding"], [issue.code for issue in issues])
        self.assertIn("0—4秒", issues[0].message)

    def test_warns_on_backlight_and_loud(self) -> None:
        prompt = "0—30秒：逆光下他大声笑。"

        codes = [issue.code for issue in validate_prompt(prompt, duration=30)]

        self.assertEqual(["risky-word", "risky-word"], codes)

    def test_reference_examples_pass(self) -> None:
        import re

        for path in (REPO_ROOT / "references").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            pattern = r"<!-- validated-example-start -->\s*```text\n(.*?)```"
            for example in re.findall(pattern, text, re.S):
                with self.subTest(path=path.name):
                    self.assertEqual([], validate_prompt(example, duration=30))

    def test_cli_returns_nonzero_and_json_for_invalid_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            prompt_path = Path(directory) / "prompt.txt"
            prompt_path.write_text("全片30秒，16:9。\n0—30秒【内容】：角色走近。", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    str(prompt_path),
                    "--duration",
                    "30",
                    "--json",
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )

        self.assertEqual(1, result.returncode)
        self.assertIn('"code": "ui-parameter"', result.stdout)
        self.assertIn('"code": "time-title"', result.stdout)


if __name__ == "__main__":
    unittest.main()
