import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TechnologySelectionTests(unittest.TestCase):
    def test_skill_routes_to_technology_selection(self):
        s = (ROOT/'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('references/technology-selection.md', s)
        self.assertIn('qualunque altro stack', s)
        self.assertNotIn('Scegli **uno** tra', s)

    def test_allows_user_choice_and_repo_detection(self):
        s = (ROOT/'references/technology-selection.md').read_text(encoding='utf-8')
        self.assertIn('Richiesta esplicita', s)
        self.assertIn('Progetto esistente', s)
        self.assertIn('Progetto nuovo', s)
        self.assertIn('non soltanto quelle documentate', s)

if __name__ == '__main__':
    unittest.main()
