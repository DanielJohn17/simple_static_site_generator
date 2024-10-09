#!/usr/bin/env python3


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

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        text = self.text
        text_type = self.text_type
        url = self.url

        return f"{class_name}({text}, {text_type}, {url})"
