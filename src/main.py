from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
  dummy = LeafNode("a", "Click me!", {"href": "https://www.google.com"}) 
  print("result ->", dummy.to_html())

main()