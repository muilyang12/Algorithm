# 155. Min Stack
# https://leetcode.com/problems/min-stack/


import math


class StackElement:
    def __init__(self, val: int, current_minimum: int):
        self.val = val
        self.current_minimum = current_minimum


class MinStack:
    def __init__(self):
        self.values = []
        self.minimum = math.inf

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)

        element = StackElement(val, self.minimum)
        self.values.append(element)

    def pop(self) -> None:
        self.values.pop()

        if not self.values:
            self.minimum = math.inf
        else:
            self.minimum = self.values[-1].current_minimum

    def top(self) -> int:
        return self.values[-1].val

    def getMin(self) -> int:
        return self.values[-1].current_minimum
