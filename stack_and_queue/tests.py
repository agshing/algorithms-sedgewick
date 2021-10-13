#!/usr/bin/env python3

import unittest
from stack import Stack
from queue import Queue


class StackAndQueueTests(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        self.assertEqual(stack.is_empty(), False)
        self.assertEqual(stack.pop(), 9)
        for i in range(8, -1, -1):
            self.assertEqual(stack.pop(), i)
        # pop empty stack
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.is_empty(), True)

    def test_queue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(queue.dequeue(), 0)
        for i in range(1, 10):
            self.assertEqual(queue.dequeue(), i)
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.is_empty(), True)


if __name__ == '__main__':
    unittest.main()
