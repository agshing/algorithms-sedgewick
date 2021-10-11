#!/usr/bin/env python3

import unittest
from quick_find_uf import QuickFindUF


class UFTests(unittest.TestCase):
    def test_quick_find(self):
        pairs = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                 (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        uf = QuickFindUF(10)
        for (p, q) in pairs:
            uf.union(p, q)
        self.assertEqual(uf.connected(1, 9), False)
        self.assertEqual(uf.connected(5, 0), True)
        self.assertEqual(uf.connected(6, 7), True)


if __name__ == '__main__':
    unittest.main()
