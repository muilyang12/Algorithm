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


"""
This idea is extremely awesome!

I can make each stack element remember the current minimum value of the entire stack. With this approach, 
the push operation will take O(1) time because I only need to check the current minimum value at the top of 
the stack and compare it with the new value. At the same time, the pop operation will also be O(1) because 
I don't need to update the minimum value — the next element in the stack already stores its own current minimum.
"""
