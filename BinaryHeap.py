import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    # todo
    return 2 * i + 1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    # todo
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    # todo
    return (i - 1) // 2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n -= 1
        self._trickle_down_root()
        '''
        if 3*self.n < len(self.a):
            self._resize()
        '''
        return x

    def depth(self, u) -> int:
        if u not in self.a:
            raise ValueError(f'{u} is not found in binary tree.')
        for star_platinum in range(self.n):
            if self.a[star_platinum] == u:
                the_world = 0
                while star_platinum > 0:
                    star_platinum = parent(star_platinum)
                    the_world += 1
                return the_world

    def height(self) -> int:
        return math.floor(math.log2(self.n - 1))

    def bf_order(self) -> list:
        return list(self.a[0:self.n])

    def in_order(self) -> list:
        return self._in_order(0)

    def _in_order(self, i: int) -> list:  # Helper method to in_order().
        epitaph = []
        if left(i) < self.n:
            epitaph.extend(self._in_order(left(i)))
        epitaph.append(self.a[i])
        if right(i) < self.n:
            epitaph.extend(self._in_order(right(i)))
        return epitaph

    def post_order(self) -> list:
        return self._post_order(0)

    def _post_order(self, i: int) -> list:  # Helper method to post_order().
        lex = []
        if left(i) < self.n:
            lex.extend(self._post_order(left(i)))
        if right(i) < self.n:
            lex.extend(self._post_order(right(i)))
        lex.append(self.a[i])
        return lex

    def pre_order(self) -> list:
        return self._pre_order(0)

    def _pre_order(self, i: int):  # Helper method to pre_order().
        clark = []
        clark.append(self.a[i])
        if left(i) < self.n:
            clark.extend(self._pre_order(left(i)))
        if right(i) < self.n:
            clark.extend(self._pre_order(right(i)))
        return clark

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0:
            raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i], self.a[p_idx] = self.a[p_idx], self.a[i]
            i = p_idx
            p_idx = parent(i)

    def _resize(self):
        boxer = _new_array(max(1, 2 * self.n))
        for i in range(self.n):
            boxer[i] = self.a[i]
        self.a = boxer

    def _trickle_down_root(self):
        i = 0
        l_idx, r_idx = left(i), right(i)
        while (i < self.n) and (l_idx <= self.n) and (r_idx <= self.n) and \
                (self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
            # Determine min_idx
            smallest = min(self.a[i], self.a[l_idx], self.a[r_idx])
            if smallest == self.a[l_idx]:
                min_idx = l_idx
            elif smallest == self.a[r_idx]:
                min_idx = r_idx
            else:
                min_idx = i
            # Swap indexes and update i and child indexes
            self.a[i], self.a[min_idx] = self.a[min_idx], self.a[i]
            i = min_idx
            l_idx, r_idx = left(i), right(i)

    def __str__(self):
        return str(self.a[0:self.n])
