# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # time complexity: O(m)
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []

        start_node = ListNode(0, head)
        pointer = start_node.next

        while pointer:
            stack.append(pointer)

            pointer = pointer.next

        if len(stack) == 1:
            return None

        if n > 1 and n < len(stack):
            stack[-n - 1].next = stack[-n + 1]
        elif n == 1:
            stack[-2].next = None
        else:
            start_node.next = stack[1]

        return start_node.next

    # O O O O O & 3
    # O & 1
    # time complexity: O(m)
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start_node = ListNode(0, head)

        fast = head
        target = head
        target_before = start_node

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            target = target.next
            target_before = target_before.next

        target_before.next = target.next

        return start_node.next
