#!/usr/bin/env python3
from typing import Dict, List
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: List[object],
            props: Dict = None
        ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required!!")
        if not self.children:
            raise ValueError("Children is required!!")

        def render_children(children):
            if not children:
                return ""
            return children[0].to_html() + render_children(children[1:])

        return render_children(self.children)
