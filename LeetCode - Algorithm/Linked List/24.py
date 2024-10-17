# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        before = dummy

        while before.next and before.next.next:
            target1 = before.next
            target2 = before.next.next

            before.next = target2
            target1.next = target2.next
            target2.next = target1

            before = target1

        return dummy.next
