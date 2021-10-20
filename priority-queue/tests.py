#!/usr/bin/env python3

import unittest
import random
import string
from pq import *


class PQTests(unittest.TestCase):
    def test_pq(self):
        capacity = 10
        pq = MaxPQ(capacity)
        test_data = []
        for i in range(capacity):
            random_letter = random.choice(string.ascii_uppercase)
            pq.insert(random_letter)
            test_data.append(random_letter)
        pq_data = [pq.del_max() for i in range(capacity)]
        self.assertEqual(pq_data, sorted(test_data, reverse=True))


if __name__ == '__main__':
    unittest.main()
