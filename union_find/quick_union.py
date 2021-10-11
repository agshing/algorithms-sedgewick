#!/usr/bin/env python3


class QuickUnion:
    def __init__(self, n: int) -> None:
        self.n = n
        # id is reserved keyword in python
        self.ids = [i for i in range(n)]

    def root(self, i: int) -> int:
        while i != self.ids[i]:
            i = self.ids[i]
        return i

    def union(self, p: int, q: int) -> None:
        p_root = self.root(p)
        q_root = self.root(q)
        self.ids[p_root] = q_root

    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)


class WeightedQuickUnion(QuickUnion):
    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.size = [1] * n

    def union(self, p: int, q: int) -> None:
        p_root = self.root(p)
        q_root = self.root(q)
        if self.size[p] < self.size[q]:
            self.ids[p_root] = q_root
            self.size[q] += self.size[p]
        else:
            self.ids[q_root] = p_root
            self.size[p] += self.size[q]