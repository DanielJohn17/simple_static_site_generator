#!/usr/bin/python3
import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("p", "Hello, I'm a leaf node")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, I'm a leaf node")
        self.assertEqual(node.children, None)
        self.assertNotEqual(node.props, [])

        node_2 = LeafNode("a", "Click me!", props={"href": "https://www.example.com"})
        self.assertEqual(node_2.tag, "a")
        self.assertEqual(node_2.value, "Click me!")
        self.assertEqual(node_2.children, None)
        self.assertEqual(node_2.props, {"href": "https://www.example.com"})

    def test_to_html(self):
        node = LeafNode("p", "Hello, I'm a leaf node")
        self.assertEqual(node.to_html(), "<p>Hello, I'm a leaf node</p>")

        node_2 = LeafNode("a", "Click me!", props={"href": "https://www.example.com"})
        self.assertEqual(node_2.to_html(), '<a href="https://www.example.com">Click me!</a>')

        node_3 = LeafNode(None, "Plain text")
        self.assertEqual(node_3.to_html(), "Plain text")

        node_4 = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node_4.to_html()


if __name__ == "__main__":
    unittest.main()