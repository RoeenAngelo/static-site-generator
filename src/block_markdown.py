from enum import Enum
from htmlnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_type_to_html_node(block))
    return ParentNode("div", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def block_type_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        text = " ".join(block.split("\n"))
        return ParentNode("p", text_to_children(text))
    
    if block_type == BlockType.HEADING:
        if block.startswith("# "):
            text = block[2:]
            return ParentNode("h1", text_to_children(text))
        if block.startswith("## "):
            text = block[3:]
            return ParentNode("h2", text_to_children(text))
        if block.startswith("### "):
            text = block[4:]
            return ParentNode("h3", text_to_children(text))
        if block.startswith("#### "):
            text = block[5:]
            return ParentNode("h4", text_to_children(text))
        if block.startswith("##### "):
            text = block[6:]
            return ParentNode("h5", text_to_children(text))
        if block.startswith("###### "):
            text = block[7:]
            return ParentNode("h6", text_to_children(text))
        
    if block_type == BlockType.CODE:
        text = block[4:-3]
        raw_node = TextNode(text, TextType.TEXT)
        child = text_node_to_html_node(raw_node)
        code = ParentNode("code", [child])
        return ParentNode("pre", [code])

    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            new_lines.append(line.lstrip(">").strip())
        text = " ".join(new_lines)
        return ParentNode("blockquote", text_to_children(text))
    
    if block_type == BlockType.ULIST:
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item[2:]
            html_items.append(ParentNode("li", text_to_children(text)))
        return ParentNode("ul", html_items)

    if block_type == BlockType.OLIST:
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item.split(". ", 1)[1]
            html_items.append(ParentNode("li", text_to_children(text)))
        return ParentNode("ol", html_items)



def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            filtered_blocks.append(stripped_block)
    return filtered_blocks

