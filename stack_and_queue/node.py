#!/usr/bin/env python3

from typing import Any

class Node:
    def __init__(self):
        self.item: Any = None
        self.next: Node = None