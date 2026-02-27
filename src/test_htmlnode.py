import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    # Test that props_to_html correctly formats attributes.
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    # Test that an empty props dictionary returns an empty string.
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p")
        expected = ''
        self.assertEqual(node.props_to_html(), expected)

    # Test that __repr__ returns a string representation of the node.
    def test_repr(self):
        node = HTMLNode(
            tag="a",
            value="Sample",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected = "HTMLNode(tag=a, value=Sample, children=None, props={'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(repr(node), expected)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    