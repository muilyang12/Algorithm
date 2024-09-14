# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        current = head

        while current:
            if current in visited:
                return True

            visited.add(current)

            current = current.next

        return False
