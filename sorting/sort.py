#!/usr/bin/env python3

from typing import List


def selection_sort(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


def insertion_sort(numbers: List[int]) -> List[int]:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, 0, -1):
            if numbers[j] < numbers[j - 1]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            else:
                break
    return numbers


def shell_sort(numbers: List[int]) -> List[int]:
    n = len(numbers)
    h = 1
    while h < n // 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and numbers[j] < numbers[j - h]:
                numbers[j], numbers[j - h] = numbers[j - h], numbers[j]
                j -= h
        h = h // 3
    return numbers
