from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SingleReadmeRefactorTest(unittest.TestCase):
    def test_readme_has_single_source_of_truth_sections(self) -> None:
        readme = (ROOT / "README.md").read_text()

        expected_sections = [
            "# 🎥 Awesome Egocentric Video Datasets",
            "## Overview",
            "## Aim",
            "## Papers & Surveys",
            "## 🎬 Video Generation & World-Model Pretraining",
            "## 🧠 Memory, Summarization & Long-form Understanding",
            "## 💬 VLMs, Instructions & QA",
            "## 🏃 Action & Activity Recognition",
            "## ✋ Hand–Object Interaction, Dexterity & 3D",
            "## 📋 Procedural Activities & Skill Learning",
            "## 🗺️ 3D Scene Understanding & Localization",
            "## 🛠️ Tools & Libraries",
            "## 🔗 Related Awesome Lists",
            "## 🤝 Contributing",
            "## License",
        ]

        for section in expected_sections:
            self.assertIn(section, readme)

    def test_readme_drops_legacy_navigation(self) -> None:
        readme = (ROOT / "README.md").read_text()

        forbidden = [
            "datasets.md",
            "benchmarks.md",
            "tasks/",
            "Repository structure",
            "Task files (`tasks/`)",
        ]

        for marker in forbidden:
            self.assertNotIn(marker, readme)

    def test_contributing_points_to_readme_sections_only(self) -> None:
        contributing = (ROOT / "CONTRIBUTING.md").read_text()

        self.assertIn("README.md", contributing)
        self.assertNotIn("datasets.md", contributing)
        self.assertNotIn("benchmarks.md", contributing)
        self.assertNotIn("tasks/", contributing)

    def test_legacy_indexes_are_removed(self) -> None:
        self.assertFalse((ROOT / "datasets.md").exists())
        self.assertFalse((ROOT / "benchmarks.md").exists())
        self.assertFalse(any((ROOT / "tasks").glob("*.md")))


if __name__ == "__main__":
    unittest.main()
