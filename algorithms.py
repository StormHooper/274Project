"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for i, j in enumerate(a):
        if j == x:
            return i
    return None


def binary_search(a: List, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        m = (left + right) // 2
        if x == a[m]:
            return m
        elif x < a[m]:
            right = m - 1
        else:
            left = m + 1
    return None


def _merge(a0: List, a1: List, a: List):
    # Step 1 and 2.
    i_0, i_1 = 0, 0
    # Step 3.
    for i in range(len(a)):
        if i_0 == len(a0):
            a[i] = a1[i_1]
            i_1 += 1
        elif i_1 == len(a1):
            a[i] = a0[i_0]
            i_0 += 1
        elif a0[i_0] <= a1[i_1]:
            a[i] = a0[i_0]
            i_0 += 1
        else:
            a[i] = a1[i_1]
            i_1 += 1


def merge_sort(a: List):
    if len(a) <= 1:  # If list already sorted.
        return a
    m = len(a) // 2
    a_0 = a[0:m]
    a_1 = a[m:len(a)]
    merge_sort(a_0)
    merge_sort(a_1)
    return _merge(a_0, a_1, a)


def _quick_sort_f(a: List, start, end):
    if start >= end:  # List already sorted.
        return
    pivot = a[start]
    i = start + 1
    #  Find where j element is less than pivot. Swap elements i and j.
    for j in range(start + 1, end + 1):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    # Swap pivot. Sort left and right lists.
    a[start], a[i - 1] = a[i - 1], a[start]
    _quick_sort_f(a, start, i - 2)
    _quick_sort_f(a, i, end)


def _quick_sort_r(a: List, start, end):
    if start >= end:  # List already sorted
        return
    # Choose random idx for pivot and swap with first element.
    p_idx = random.randint(start, end)
    a[start], a[p_idx] = a[p_idx], a[start]
    pivot = a[start]
    # For the rest, similar logic to _quick_sort_f()
    i = start + 1
    # Find where j element is less than pivot. Swap elements i and j.
    for j in range(start + 1, end + 1):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    # Swap pivot. Sort left and right lists.
    a[start], a[i - 1] = a[i - 1], a[start]
    _quick_sort_r(a, start, i - 2)
    _quick_sort_r(a, i, end)


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)
