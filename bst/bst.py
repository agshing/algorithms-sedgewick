#!/usr/bin/env python3
from typing import Any, Optional, List


class Node:
    def __init__(self, key: Any, val: Any) -> None:
        self.key = key
        self.val = val
        self.left: "Node" = None
        self.right: "Node" = None


class BST:
    def __init__(self) -> None:
        self.root: Node = None

    def put(self, key: Any, val: Any) -> None:
        def put_node(x: Node, key: Any, val: Any) -> Node:
            if x == None:
                return Node(key=key, val=val)
            if key > x.key:
                x.right = put_node(x.right, key, val)
            elif key < x.key:
                x.left = put_node(x.left, key, val)
            else:
                # key exist, override the value
                x.val = val
            return x

        self.root = put_node(self.root, key, val)

    def get(self, key: Any) -> Optional[Any]:
        x = self.root
        while x != None:
            if key > x.key:
                x = x.right
            elif key < x.key:
                x = x.left
            else:
                return x.val
        return None

    def delete(self, key: Any) -> None:
        def min_node(x: Node) -> Node:
            if x.left is None:
                return x
            return min_node(x.left)

        def delete_node(x: Node, key: Any) -> Optional[Node]:
            if x is None:
                return None
            if key < x.key:
                x.left = delete_node(x.left, key)
            elif key > x.key:
                x.right = delete_node(x.right, key)
            else:
                # found the node
                # if right node is None return left node
                if x.right is None:
                    return x.left
                # if left node is None return right node
                if x.left is None:
                    return x.right
                # if both nodes exist, replace  with successor
                t = x
                # get the min node from the right branch
                x = min_node(t.right)
                x.right = self.__delete_min(t.right)
                x.left = t.left
            return x

        self.root = delete_node(self.root, key)

    def floor(self, key: Any) -> Optional[Any]:
        def floor_node(x: Node, key: Any) -> Node:
            if x is None:
                return None
            if x.key == key:
                return x
            elif x.key > key:
                return floor_node(x.left, key)
            else:
                t = floor_node(x.right, key)
                return t if t is not None else x

        x = floor_node(self.root, key)
        return x.key if x is not None else None

    def inorder_traversal(self) -> Optional[List[Any]]:
        def traverse(x: Node, lst: List[Any]) -> None:
            if x == None:
                return
            traverse(x.left, lst)
            lst.append(x.key)
            traverse(x.right, lst)
        result = []
        traverse(self.root, result)
        return result

    def delete_min(self) -> None:
        self.root = self.__delete_min(self.root)

    def __delete_min(self, x: Node):
            if x.left == None:
                return x.right
            x.left = self.__delete_min(x.left)
            return x