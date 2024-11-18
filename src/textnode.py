#!/usr/bin/env python3
from enum import Enum
from leafnode import LeafNode



class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(
            self,
            text: str,
            text_type: str,
            url: str =None
        ) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, obj: object) -> bool:
        return self.text == obj.text and\
                self.text_type == obj.text_type and\
                self.url == obj.url
    
    @staticmethod
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode("", text_node.text).to_html()
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text).to_html()
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text).to_html()
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text).to_html()
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url}).to_html()
        elif text_node.text_type == TextType.IMAGE:
            return f'<img src="{text_node.url}" alt="{text_node.text}"/>'
        else:
            raise ValueError("Invalid text type")

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        text = self.text
        text_type = self.text_type
        url = self.url

        return f"{class_name}({text}, {text_type}, {url})"
