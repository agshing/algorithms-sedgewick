#!/usr/bin/env python3

import unittest
from quick_find import QuickFind
from quick_union import QuickUnion, WeightedQuickUnion


class UFTests(unittest.TestCase):
    def test_quick_find(self):
        pairs = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                 (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        uf = QuickFind(n=10)
        for (p, q) in pairs:
            uf.union(p, q)
        self.assertEqual(uf.connected(1, 9), False)
        self.assertEqual(uf.connected(5, 0), True)
        self.assertEqual(uf.connected(6, 7), True)

    def test_quick_union(self):
        pairs = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                 (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        uf = QuickUnion(n=10)
        for (p, q) in pairs:
            uf.union(p, q)
        self.assertEqual(uf.connected(1, 0), True)
        self.assertEqual(uf.connected(7, 2), True)
        self.assertEqual(uf.connected(6, 9), False)

    def test_weighted_quick_union(self):
        pairs = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                 (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        uf = WeightedQuickUnion(n=10)
        for (p, q) in pairs:
            uf.union(p, q)
        self.assertEqual(uf.connected(2, 1), True)
        self.assertEqual(uf.connected(7, 8), False)
        self.assertEqual(uf.connected(4, 8), True)


if __name__ == '__main__':
    unittest.main()
