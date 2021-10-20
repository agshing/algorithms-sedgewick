#!/usr/bin/env python3

import unittest
from bst import *


class BSTTests(unittest.TestCase):
    def test_bst(self):
        # create list of char: ascii_code tuples
        key_val_lst = [(c, ord(c)) for c in "PSEUDOMYTHICAL"]
        bst = BST()
        for key, val in key_val_lst:
            bst.put(key, val)
        # inorder traversal must  return keys in sorted order
        self.assertEqual(bst.inorder_traversal(), sorted(
            [key for key, _ in key_val_lst]))
        # check existing node
        self.assertEqual(bst.get("Y"), ord("Y"))
        # check non existing node
        self.assertEqual(bst.get("G"), None)
        # check floor for existing node
        self.assertEqual(bst.floor("P"), "P")
        # check floor for non existing node
        self.assertEqual(bst.floor("G"), "E")
        # test delete
        for key, _ in key_val_lst:
            bst.delete(key)
            self.assertEqual(bst.get(key), None)


if __name__ == '__main__':
    unittest.main()
