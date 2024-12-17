from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
  text_node = TextNode("hello world!", TextType.BOLD, "https://www.google.com")
  print(text_node_to_html_node(text_node))
  

main()