#!/usr/bin/env python3


class QuickFind:
    def __init__(self, n: int) -> None:
        self.n = n
        # id is reserved keyword in python
        self.ids = [i for i in range(n)]

    def union(self, p: int, q: int) -> None:
        pid = self.ids[p]
        qid = self.ids[q]
        for i in range(self.n):
            if self.ids[i] == pid:
                self.ids[i] = qid

    def connected(self, p: int, q: int) -> bool:
        return self.ids[p] == self.ids[q]
