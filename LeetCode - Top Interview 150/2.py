# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = current = ListNode()

        l1_ptr = l1
        l2_ptr = l2

        has_carry = None

        while l1_ptr or l2_ptr:
            value = None

            if l1_ptr and not l2_ptr:
                value = l1_ptr.val
                l1_ptr = l1_ptr.next

            elif not l1_ptr and l2_ptr:
                value = l2_ptr.val
                l2_ptr = l2_ptr.next

            else:
                value = l1_ptr.val + l2_ptr.val
                l1_ptr = l1_ptr.next
                l2_ptr = l2_ptr.next

            if has_carry:
                value += 1
                has_carry = False

            if value >= 10:
                value -= 10
                has_carry = True

            current.next = ListNode(value, None)
            current = current.next

        if has_carry:
            current.next = ListNode(1, None)

        return dummy.next
