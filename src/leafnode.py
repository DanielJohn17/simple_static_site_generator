#!/usr/bin/python3
from typing import Dict, List
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            value: str,
            props: Dict = None
        ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")

        if not self.tag:
            return self.value
        
        if self.props:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'

