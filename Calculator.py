import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator
import re

class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for i in s:
            if i == '(':
                stack.push(i)
            elif i == ')':
                try:
                    stack.pop()
                except IndexError:
                    return False
        if stack.n == 0:
            return True
        return False

    def print_expression(self, exp: str):
        # Separate the variables
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        everything_else = re.split('\w+', exp)
        # Print the expression
        expression = ""
        for i in range(len(variables)):
            expression += everything_else[i]
            expression += variables[i]
        for variable in variables:
            if self.dict.find(variable) is not None and variable != '':
                expression = expression.replace(variable, str(self.dict.find(variable)))
        print(expression)
        return expression

    def _build_parse_tree(self, exp: str) -> str:
        # todo
        if not self.matched_expression(exp):
            raise ValueError
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        exp = re.findall('[-+*/()]|\w+', exp)
        bt = BinaryTree.BinaryTree()
        bt.r = bt.Node()
        current = bt.r
        for i in exp:
            node = bt.Node()
            if i == '(':
                current = current.insert_left(node)
            elif i in '+-*/':
                current.set_val(i)
                current.set_key(i)
                current = current.insert_right(node)
            elif i in variables:
                current.set_key(i)
                current.set_val(self.dict.find(i))
                current = current.parent
            elif i == ')':
                current = current.parent
        return bt
    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        # todo
        if root.left is not None and root.right is not None:
            fink = op[root.k]
            return fink(self._evaluate(root.left), self._evaluate(root.right))
        elif root.left is None and root.right is None:
            if root.v is not None:
                return float(root.v)
            raise ValueError(f"Missing value for variable {root.k}")
        elif root.left is not None:
            return self._evaluate(root.left)
        else:
            return self._evaluate(root.right)


    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)
