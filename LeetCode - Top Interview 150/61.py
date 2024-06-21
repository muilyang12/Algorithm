# 61. Rotate List
# https://leetcode.com/problems/rotate-list/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # time complexity: O(2n) = O(n)
    def rotateRight1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return None

        count = 0
        count_ref = head
        while count_ref:
            count += 1
            count_ref = count_ref.next

        adjusted_k = k % count

        if adjusted_k == 0:
            return head

        fast = head
        slow = head

        for _ in range(adjusted_k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        first_node = ListNode(0, slow.next)
        fast.next = head
        slow.next = None

        return first_node.next

    # time complexity: O(2n - k) = O(n)
    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head

        last_node = head

        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1

        adjusted_k = k % length

        if adjusted_k == 0:
            return head

        new_last_node = head
        for _ in range(length - adjusted_k - 1):
            new_last_node = new_last_node.next

        answer = new_last_node.next
        new_last_node.next = None
        last_node.next = head

        return answer
