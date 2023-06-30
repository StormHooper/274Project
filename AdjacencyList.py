"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        if not self.has_edge(i, j):
            self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) -> bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        incoming = []
        for k in range(self.n):
            if self.has_edge(k, i):
                incoming.append(k)
        return incoming

    def bfs(self, r : int):
        traversal = ArrayList.ArrayList()
        seen = [False for i in range(self.n)]
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while q.n > 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for element in neighbors:
                if seen[element] is False:
                    q.add(element)
                    traversal.append(element)
                    seen[element] = True
        return traversal

    def dfs(self, r : int):
        # todo
        traversal = ArrayList.ArrayList()
        stack = ArrayStack.ArrayStack()
        seen = [False for i in range(self.n)]
        stack.push(r)
        while stack.n > 0:
            current = stack.pop()
            if seen[current] is False:
                traversal.append(current)
                seen[current] = True
            neighbors = reversed(self.out_edges(current))
            for j in neighbors:
                if seen[j] is False:
                    stack.push(j)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

    def size(self):
        return self.n
