
class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    keys = list(self.props.keys())
    values = list(self.props.values())
    new_str = ""
    for i in range(0, len(keys)):
      new_str += f' {keys[i]}="{values[i]}"'
    
    return new_str