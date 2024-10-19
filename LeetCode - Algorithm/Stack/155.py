# 155. Min Stack
# https://leetcode.com/problems/min-stack/

from typing import List
import math


class MinStackElement:
    def __init__(self, value, minSoFar):
        self.value = value
        self.currentMin = min(minSoFar, value)


class MinStack:
    def __init__(self):
        self.stack: List[MinStackElement] = []

    def push(self, val: int) -> None:
        if self.stack:
            minSoFar = self.stack[-1].currentMin
        else:
            minSoFar = math.inf

        stackElement = MinStackElement(val, minSoFar)

        self.stack.append(stackElement)

    def pop(self) -> None:
        if not self.stack:
            return

        lastElement = self.stack.pop()

        return lastElement.value

    def top(self) -> int:
        if not self.stack:
            return

        lastElement = self.stack[-1]

        return lastElement.value

    def getMin(self) -> int:
        if not self.stack:
            return

        lastElement = self.stack[-1]

        return lastElement.currentMin
