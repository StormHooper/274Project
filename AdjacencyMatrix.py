from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        # todo
        self.adj[i][j] = True

    def remove_edge(self, i : int, j : int):
        # todo
        if not self.adj[i][j]:
            return False
        self.adj[i][j] = False
        return True

    def has_edge(self, i : int, j: int) -> bool:
        # todo
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        duck = ArrayList.ArrayList()
        for quack in range(self.n):
            if self.adj[i][quack] == 1:
                duck.append(quack)
        return duck

    def in_edges(self, j) -> List:
        carl = ArrayList.ArrayList()
        for junior in range(self.n):
            if self.adj[junior][j] == 1:
                carl.append(junior)
        return carl

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

    def size(self):
        return self.n
