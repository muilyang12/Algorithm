# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        current = head
        next = head.next

        while next:
            current.next = prev

            prev = current
            current = next
            next = next.next

        current.next = prev

        return current
