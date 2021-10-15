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


def merge_sort(numbers: List[int]) -> List[int]:
    def merge(numbers: List[int], aux: List[int], left: int, mid: int, right: int) -> None:
        # copy data to aux list
        for k in range(left, right + 1):
            aux[k] = numbers[k]
        # data is sorted between left : mid and mid+1 : right
        i, j = left, mid + 1
        for k in range(left, right + 1):
            if i > mid:
                numbers[k] = aux[j]
                j += 1
            elif j > right:
                numbers[k] = aux[i]
                i += 1
            elif aux[i] > aux[j]:
                numbers[k] = numbers[j]
                j += 1
            else:
                numbers[k] = aux[i]
                i += 1

    def sort(numbers: List[int], aux: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        mid = left + (right - left) // 2
        sort(numbers, aux, left, mid)
        sort(numbers, aux, mid + 1, right)
        # if biggest item in the first half is <= smallest item in the second half
        # then data is already sorted, no need for the merge
        if numbers[mid] <= numbers[mid + 1]:
            return
        merge(numbers, aux, left, mid, right)

    # pass aux list as parameter to prevent creation of new lists
    aux = numbers[:]
    sort(numbers, aux, 0, len(numbers) - 1)
    return numbers
