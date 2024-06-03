# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before_left_node = None
        after_right_node = None

        before_left_node = dummy
        for _ in range(left - 1):
            before_left_node = before_left_node.next

        stack = []
        current = before_left_node.next
        for _ in range(right - left + 1):
            stack.append(current)
            current = current.next
        after_right_node = current

        current = before_left_node
        for _ in range(right - left + 1):
            current.next = stack.pop()
            current = current.next

        current.next = after_right_node

        return dummy.next


solution = Solution()

print(solution.reverseBetween(head=[1, 2, 3, 4, 5], left=2, right=4))
print(solution.reverseBetween(head=[5], left=1, right=1))
