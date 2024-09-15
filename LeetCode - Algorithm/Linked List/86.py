# 86. Partition List
# https://leetcode.com/problems/partition-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        nodesSmallerThanX = dummy1
        dummy2 = ListNode(-1)
        restNodes = dummy2

        target = head

        while target:
            if target.val < x:
                nodesSmallerThanX.next = target
                nodesSmallerThanX = nodesSmallerThanX.next
                target = target.next
                nodesSmallerThanX.next = None
            else:
                restNodes.next = target
                restNodes = restNodes.next
                target = target.next
                restNodes.next = None

        nodesSmallerThanX.next = dummy2.next

        return dummy1.next
