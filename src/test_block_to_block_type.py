import unittest
from main import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "###### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "####### This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        block = "```\nThis is a code block\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "```This is not a code block```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote\n> This is another line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "> This is a quote\nThis is not a quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        block = "- This is a list\n- This is another item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "- This is a list\n* This is not a list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is a list\n2. This is another item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "1. This is a list\n3. This is not a list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        block = "1. This is a list\n2. This is another item\n3. This is the third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        block = "This is a paragraph\nwith multiple lines"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
