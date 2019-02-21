import unittest

from dd_tag_parser import parse


class TestParse(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(
            parse('<e/>'),
            [
                {'tag': 'e', 'attributes': {}},
            ]
        )

    def test_multiple_tags(self):
        self.assertEqual(
            parse('<e/><tc/>'),
            [
                {'tag': 'e', 'attributes': {}},
                {'tag': 'tc', 'attributes': {}},
            ]
        )

    def test_attributes(self):
        self.assertEqual(
            parse('<e id="15"/>'),
            [
                {'tag': 'e', 'attributes': {'id': '15'}},
            ]
        )

    def test_multiple_attributes(self):
        self.assertEqual(
            parse('<e id="15" name="qwerty"/>'),
            [
                {
                    'tag': 'e',
                    'attributes': {
                        'id': '15',
                        'name': 'qwerty',
                    },
                },
            ]
        )

    def text_complex(self):
        self.assertEqual(
            parse('<e/><tc/><diact type="b"/>'),
            [
                {
                    'tag': 'e',
                    'attributes': {},
                },
                {
                    'tag': 'tc',
                    'attributes': {},
                },
                {
                    'tag': 'diact',
                    'attributes': {'type': 'b'},
                },
            ]
        )


if __name__ == '__main__':
    unittest.main()
