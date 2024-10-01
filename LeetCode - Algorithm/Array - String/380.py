# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:
    def __init__(self):
        self.data = []
        self.valueToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.valueToIndex:
            return False

        self.data.append(val)
        self.valueToIndex[val] = len(self.data) - 1

        return True

    def remove(self, val: int) -> bool:
        if val in self.valueToIndex:
            targetIndex = self.valueToIndex[val]

            if targetIndex != len(self.data) - 1:
                del self.valueToIndex[self.data[targetIndex]]

                self.data[targetIndex] = self.data[-1]
                self.valueToIndex[self.data[-1]] = targetIndex
                self.data.pop()
            else:
                del self.valueToIndex[self.data[targetIndex]]

                self.data.pop()

            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.data)


"""
If we just want to add and remove elements in O(1), we could use a 'set()', which is very straightforward. 
However, since we need to use 'random.choice(Array)', we have to use an array for 'self.data'. To achieve 
O(1) removal with an array, we can use a combination of an array and a 'valueToIndex' hash map to keep 
track of element positions.

This is a very interesting method where we remove the element we want to remove by replacing it with 
the last element in the list. In this scenario, the order of elements in `self.data` is not important, 
so we can freely swap the target element with the last one. The `del` operator would take O(n) time 
due to shifting elements, but by moving the last element to the position of the target index, we reduce 
the removal operation to O(1) complexity.
"""
