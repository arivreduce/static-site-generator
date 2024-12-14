import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

  def test_eq_false(self):
    node1 = HTMLNode('a', 'website', None, {
      'href': 'https://www.google.com', 'target': '_blank'
    })
    node2 = HTMLNode('p', 'website', None, {
      'href': 'https://www.google.com', 'target': '_blank'
    })
    self.assertNotEqual(node1, node2)

  def test_repr(self):
    node = HTMLNode('p', 'website', None, {
      'href': 'https://www.google.com', 'target': '_blank'
    })
    self.assertEqual("HTMLNode(p, website, None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node))
  
  def test_props_to_html(self):
    node = HTMLNode('p', 'website', None, {
      'href': 'https://www.google.com', 'target': '_blank'
    })
    result = node.props_to_html()
    self.assertEqual(result, ' href="https://www.google.com" target="_blank"')