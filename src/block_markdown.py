from htmlnode import ParentNode
from helpers import block_to_html_node

bigger_numbers = """1. First
2. Second
3. Third
4. Fourth
5. Fifth
6. Sixth
7. Seventh
8. Eighth
9. Ninth
10. Tenth"""

def markdown_to_blocks(markdown):
  blocks = markdown.split("\n\n")
  new_blocks = []
  for block in blocks:
    if block == "":
      continue
    block = block.strip()
    new_blocks.append(block)
  return new_blocks
  
def markdown_to_html_node(md):
  blocks = markdown_to_blocks(md)
  children = []
  for block in blocks:
    html_node = block_to_html_node(block)
    children.append(html_node)
  return ParentNode("div", children)
