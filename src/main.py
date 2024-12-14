from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
  dummy = HTMLNode("p", "hello world", None, {
    "href": "https://www.google.com", 
    "target": "_blank",
  })  
  print("result ->", dummy.props_to_html())

main()