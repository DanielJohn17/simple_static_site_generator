# !/usr/bin/env python3
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("p")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, None)
        self.assertNotEqual(node.value, "")
        self.assertEqual(node.children, None)
        self.assertNotEqual(node.props, [])
        self.assertEqual(node.props, None)
        self.assertNotEqual(node.props, {})

    def test_props_to_html(self):
        node = HTMLNode("p", props={"class": "para"})
        self.assertEqual(node.props_to_html(), 'class="para" ')

    def test_repr(self):
        node = HTMLNode("p", value="Hello, World!", props={"class": "para"})
        self.assertEqual(
            repr(node),
            """HTMLNode(
            tag: p,
            value: Hello, World!,
            children: None,
            props: {'class': 'para'}

            class="para" 
        )""",
        )

    def test_child_tag(self):
        node = HTMLNode("p", children=[HTMLNode("span")])
        self.assertEqual(node.children[0].tag, "span")

if __name__ == "__main__":
    unittest.main()
