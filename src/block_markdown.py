# Should return True
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
    

print(is_ordered_list(bigger_numbers))