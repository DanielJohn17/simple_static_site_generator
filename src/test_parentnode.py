#!/usr/bin/env python3
import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        parent = ParentNode("div", [], {"class": "container"})
        self.assertEqual(parent.tag, "div")
        self.assertEqual(parent.props, {"class": "container"})
        self.assertEqual(parent.children, [])
        self.assertRaises(ValueError, parent.to_html)

    def test_parent_node_with_invalid_tag(self):
        parent = ParentNode("", [], {"class": "container"})
        self.assertRaises(ValueError, parent.to_html)

    def test_parent_node_with_children(self):
        child1 = LeafNode("p", "Hello, World!")
        child2 = LeafNode("p", "Hello, Python!")
        parent = ParentNode("div", [child1, child2], {"class": "container"})
        self.assertEqual(parent.tag, "div")
        self.assertEqual(parent.props, {"class": "container"})
        self.assertEqual(parent.children, [child1, child2])
        self.assertEqual(parent.to_html(), "<p>Hello, World!</p><p>Hello, Python!</p>")

    def test_parent_node_with_children_and_invalid_tag(self):
        child1 = LeafNode("p", "Hello, World!")
        child2 = LeafNode("p", "Hello, Python!")
        parent = ParentNode("", [child1, child2], {"class": "container"})
        self.assertRaises(ValueError, parent.to_html)

if __name__ == "__main__":
    unittest.main()