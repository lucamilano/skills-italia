import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from pa_audit import scan_text, scan_path


class AuditTest(unittest.TestCase):
    def rules(self, html):
        return {f['rule'] for f in scan_text(html, 'test.html')}

    def test_img_without_alt(self):
        self.assertIn('img-alt', self.rules('<main><img src="a.png"></main>'))

    def test_good_semantic_html(self):
        html = '<html lang="it"><main><label for="x">Nome</label><input id="x"><img src="a" alt=""></main></html>'
        self.assertFalse(self.rules(html))

    def test_input_without_label(self):
        self.assertIn('input-name', self.rules('<input id="x" type="text">'))

    def test_wrap_label(self):
        self.assertNotIn('input-name', self.rules('<label>Nome <input type="text"></label>'))

    def test_duplicate_ids(self):
        self.assertIn('duplicate-id', self.rules('<input id="same"><div id="same"></div>'))

    def test_whole_document(self):
        rules = self.rules('<html><body><p>Test</p></body></html>')
        self.assertIn('html-lang', rules)
        self.assertIn('main-landmark', rules)

    def test_fixture(self):
        count, findings = scan_path(Path(__file__).parent/'fixtures')
        self.assertEqual(count, 2)
        self.assertTrue(any(i['rule']=='img-alt' for i in findings))


if __name__ == '__main__':
    unittest.main()
