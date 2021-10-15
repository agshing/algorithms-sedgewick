#!/usr/bin/env python3

import unittest
import random
from sort import *


class SortingTests(unittest.TestCase):
    def test_sort_functions(self):
        random_numbers = random.sample(range(100), 20)
        # pass copy of the list to sort functions
        self.assertEqual(selection_sort(
            random_numbers[:]), sorted(random_numbers))
        self.assertEqual(insertion_sort(
            random_numbers[:]), sorted(random_numbers))
        self.assertEqual(shell_sort(
            random_numbers[:]), sorted(random_numbers))
        self.assertEqual(merge_sort(
            random_numbers[:]), sorted(random_numbers))


if __name__ == '__main__':
    unittest.main()
