#!/usr/bin/env python3

from typing import Any


class MaxPQ:
    def __init__(self, capacity: int) -> None:
        self.pq = [None] * (capacity + 1)
        self.count = 0

    def is_empty(self) -> bool:
        return self.count == 0

    def insert(self, data: Any) -> None:
        self.count += 1
        self.pq[self.count] = data
        self.__swim(self.count)

    def del_max(self) -> Any:
        max = self.pq[1]
        self.pq[1], self.pq[self.count] = self.pq[self.count], self.pq[1]
        self.count -= 1
        self.__sink(1)
        self.pq[self.count + 1] = None
        return max

    def __swim(self, key: int) -> None:
        while key > 1 and self.pq[key] > self.pq[key // 2]:
            self.pq[key], self.pq[key // 2] = self.pq[key // 2], self.pq[key]
            key = key // 2

    def __sink(self, key: int) -> None:
        while 2 * key <= self.count:
            index = 2 * key
            # choose the largest child
            index = index + 1 if index + \
                1 <= self.count and self.pq[index] < self.pq[index + 1] else index
            if self.pq[key] > self.pq[index]:
                # item is placed correctly
                break
            self.pq[index], self.pq[key] = self.pq[key], self.pq[index]
            key = index
