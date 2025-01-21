# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        oddCurrent: Optional[ListNode] = head
        evenHead: Optional[ListNode] = head.next

        current: Optional[ListNode] = head.next
        beforeCurrent: Optional[ListNode] = head

        currentNum = 2

        while current:
            if currentNum % 2 == 1:
                beforeCurrent.next = current.next

                oddCurrent.next = current
                current.next = evenHead
                oddCurrent = oddCurrent.next

                current = beforeCurrent.next
                currentNum += 1
            else:
                beforeCurrent = current
                current = current.next
                currentNum += 1

        return head
