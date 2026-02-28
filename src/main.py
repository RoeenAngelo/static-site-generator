from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    SampleTextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    node = HTMLNode(
        tag="a",
        value="Sample",
        props={"href": "https://www.google.com", "target": "_blank"}
    )
    # print(repr(node))
    print(node)

main()