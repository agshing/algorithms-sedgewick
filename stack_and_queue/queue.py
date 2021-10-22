#!/usr/bin/env python3#!/usr/bin/env python3

from typing import Any
from node import Node


class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def enqueue(self, item: Any) -> None:
        node = Node()
        node.item = item
        node.next = None
        if self.is_empty():
            self.tail, self.head = node, node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> Any:
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        # if there is no more nodes, assign tail to None
        if self.head == None:
            self.tail = None
        node.next = None
        return node.item

    def is_empty(self):
        return self.head == None
