# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:
    def __init__(self):
        self.data = []
        self.valueToIndex = {}

    def insert(self, val: int) -> bool:
        pass

    def remove(self, val: int) -> bool:
        pass

    def getRandom(self) -> int:
        random.choice()

        pass


"""
This is a very interesting method where we remove the element we want to remove by replacing it with 
the last element in the list. In this scenario, the order of elements in `self.data` is not important, 
so we can freely swap the target element with the last one. The `del` operator would take O(n) time 
due to shifting elements, but by moving the last element to the position of the target index, we reduce 
the removal operation to O(1) complexity.
"""
