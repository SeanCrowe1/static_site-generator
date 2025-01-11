import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):
        text = "# Hello World"
        self.assertEqual(extract_title(text), "Hello World")

    def test_extract_title_from_block(self):
        text = "# Hello World\nWelcome to my presentation\nThat was it."
        self.assertEqual(extract_title(text), "Hello World")

    def test_extract_title_from_within_block(self):
        text = "Welcome to my presentation\nOh yeah\n# Hello World!\nI really messed that up..."
        self.assertEqual(extract_title(text), "Hello World!")

    def test_extract_only_title(self):
        text = "### all these hashes\n## are confusing me!\n# Hello World\n###### Can anyone hear me?!"
        self.assertEqual(extract_title(text), "Hello World")