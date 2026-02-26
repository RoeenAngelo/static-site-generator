from textnode import TextNode, TextType

def main():
    SampleTextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(SampleTextNode)
    
main()