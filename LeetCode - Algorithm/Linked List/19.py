# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        prev = ListNode(-1)
        prev.next = head

        target = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return target.next

        while fast:
            prev = prev.next
            target = target.next
            fast = fast.next

        prev.next = target.next

        return head
