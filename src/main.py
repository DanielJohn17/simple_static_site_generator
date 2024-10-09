#!/usr/bin/env python3
from textnode import TextNode


def main() -> None:
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")

    print(text_node)

if __name__ == "__main__":
    main()
