from htmlnode import ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

def is_heading(block):
  hash_count = 0
  for char in block:
    if char != "#":
      break
    hash_count += 1
  if hash_count < 1 or hash_count > 6:
    return False
  if len(block) <= hash_count:
    return False
  if block[hash_count] != " ":
    return False
  if len(block) <= hash_count + 1:
    return False
  return True
  
def is_codeblock(block):
  if len(block) < 7:
    return False
  return block[0:3] == "```" and block[-3:] == "```"

def is_quote_block(block):
  heading_list = block.split("\n")
  for line in heading_list:
    if line == "":
      continue
    if line[0] != ">":
      return False
  return True

def is_unordered_list(block):
  unordered_split = block.split("\n")
  for item in unordered_split:
    if item == "":
      continue
    if len(item) == 1:
      return False
    if item[0] != "-" and item[0] != "*":
      return False
    if item[1] != " ":
      return False
  return True

def is_ordered_list(block):
  ordered_split = block.split("\n")
  counter = 1
  for item in ordered_split:
    if item == "":
      continue
    if len(item) < 3:
      return False
    if not item[0].isdigit():
      return False
    period_index = item.find(".")
    if period_index == -1:
      return False
    number = item[0:period_index]
    if int(number) != counter or item[period_index + 1] != " ":
      return False
    counter += 1
  return True


def block_to_html_node(block):
  block_type = block_to_block_type(block)
  if block_type == "paragraph":
    return paragraph_to_html_node(block)
  if block_type == "heading":
    return heading_to_html_node(block)
  if block_type == "code":
    return code_to_html_node(block)
  if block_type == "quote":
    return quote_to_html_node(block)
  if block_type == "unordered_list":
    return unordered_to_html_node(block)
  if block_type == "ordered_list":
    return ordered_to_html_node(block)
  raise ValueError("Invalid block type")
  
def paragraph_to_html_node(block):
  lines = block.split("\n")
  paragraph = " ".join(lines)
  children = text_to_children(paragraph)
  return ParentNode("p", children)

def text_to_children(text):
  text_nodes = text_to_textnodes(text)
  children = []
  for text_node in text_nodes:
    html_node = text_node_to_html_node(text_node)
    children.append(html_node)
  return children

def heading_to_html_node(block):
  level = 0
  for char in block:
    if char == "#":
      level += 1
    else:
      break
  if level + 1 >= len(block):
    raise ValueError(f"Invalid heading level: {level}")
  text = block[level + 1:]
  children = text_to_children(text)
  return ParentNode(f"h{level}", children)

def code_to_html_node(block):
  if not block.startswith("```") or not block.endswith("```"):
    raise ValueError("Invalid code block!")
  text = block[4:-3]
  children = text_to_children(text)
  code = ParentNode("code", children)
  return ParentNode("pre", [code])

def quote_to_html_node(block):
  lines = block.split("\n")
  new_lines = []
  for line in lines:
    if not line.startswith(">"):
      raise ValueError("Invalid quote block")
    new_lines.append(line.lstrip(">").strip())
  content = " ".join(new_lines)
  children = text_to_children(content)
  return ParentNode("blockquote", children)

def unordered_to_html_node(block):
  lines = block.split("\n")
  html_items = []
  for line in lines:
    text = line[2:]
    children = text_to_children(text)
    html_items.append(ParentNode("li", children))
  return ParentNode("ul", html_items)
    
def ordered_to_html_node(block):
  lines = block.split("\n")
  html_items = []
  for line in lines:
    text = line[3:]
    children = text_to_children(text)
    html_items.append(ParentNode("li", children))
  return ParentNode("ol", html_items)

def block_to_block_type(block):
  if is_heading(block):
    return "heading"
  if is_codeblock(block):
    return "code"
  if is_quote_block(block):
    return "quote"
  if is_unordered_list(block):
    return "unordered_list"
  if is_ordered_list(block):
    return "ordered_list"
  return "paragraph"