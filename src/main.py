from textnode import TextNode, TextType

def main():
  dummy_node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
  print(dummy_node)

main()