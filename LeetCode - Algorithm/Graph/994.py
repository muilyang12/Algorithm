# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1


"""
===== Knowledge =====

from collections import deque

'deque' is a data structure in Python provided by the collections module.

When popping an element, a deque is far more efficient than a list. When we use list, inserting or deleting 
elements from the front requires shifting all subsequent elements, which takes linear time O(n). Whereas
A deque performs this operation in constant time O(1).

values = deque([1, 2, 3, 4])

values.append(5)
values.appendleft(0)

values.pop()
values.popleft()
"""
