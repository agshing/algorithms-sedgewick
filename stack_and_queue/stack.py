#!/usr/bin/env python3

from typing import Any
from node import Node


class Stack:
    def __init__(self):
        self.head: Node = None

    def push(self, item: Any) -> None:
        node = Node()
        node.item = item
        node.next = self.head
        self.head = node

    def pop(self) -> Any:
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        node.next = None
        return node.item

    def is_empty(self):
        return self.head == None
