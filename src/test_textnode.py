#!/usr/bin/env python3
import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.text_node_to_html_node(node), "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a bold text", TextType.BOLD)
        self.assertEqual(node.text_node_to_html_node(node), "<b>This is a bold text</b>")

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is an italic text", TextType.ITALIC)
        self.assertEqual(node.text_node_to_html_node(node), "<i>This is an italic text</i>")

    def test_text_node_to_html_node_code(self):
        node = TextNode("print('Hello, world!')", TextType.CODE)
        self.assertEqual(node.text_node_to_html_node(node), "<code>print('Hello, world!')</code>")

    def test_text_node_to_html_node_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node.text_node_to_html_node(node), '<a href="https://www.boot.dev">Boot.dev</a>')

    def test_text_node_to_html_node_image(self):
        node = TextNode("Boot.dev logo", TextType.IMAGE, "https://www.boot.dev/logo.png")
        self.assertEqual(node.text_node_to_html_node(node), '<img src="https://www.boot.dev/logo.png" alt="Boot.dev logo"/>')

    def test_text_node_to_html_node_invalid(self):
        node = TextNode("Invalid text type", "invalid")
        with self.assertRaises(ValueError):
            node.text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()