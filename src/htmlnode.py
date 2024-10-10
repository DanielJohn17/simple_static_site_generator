#!/usr/bin/env python3
from typing import List, Dict


class HTMLNode:
    def __init__(
            self,
            tag: str = None,
            value: str = None,
            children: List[object] = None,
            props: Dict = None
        ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        html_str = ''

        for key, value in self.props.items():
            sub_str = f'{key}="{value}" '
            html_str += sub_str

        return html_str

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        tag = self.tag
        value = self.value
        childern = self.children
        props = self.props

        class_repr = f"""{class_name}(
            tag: {tag},
            value: {value},
            children: {childern},
            props: {props}

            {self.props_to_html()}
        )"""
        
        return class_repr
