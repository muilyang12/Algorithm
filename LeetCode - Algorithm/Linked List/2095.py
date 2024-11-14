# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        before = dummy

        slow = head
        fast = head

        while fast and fast.next:
            before = slow
            slow = slow.next
            fast = fast.next.next

        before.next = slow.next

        return dummy.next
