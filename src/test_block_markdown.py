import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks
        )
    

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks
        )


    # Tests for block_to_block_type
    def test_block_to_block_types(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        block = "```\nThis is a code\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
        block = ">quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        block = "1. list\n2. another list"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        
        block = "- list\n- another list"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)

        block = "# h1\n ## h2\n ### h3\n #### h4\n ##### h5\n ###### h6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)