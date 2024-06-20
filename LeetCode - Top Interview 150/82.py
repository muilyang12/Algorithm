# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # time complexity: O(n)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start_node = ListNode(-500, head)

        if not head or not head.next:
            return head

        first = start_node
        second = head
        third = head.next

        while first and second and third:
            if second.val == third.val:
                while third and second.val == third.val:
                    third = third.next

                if not third:
                    first.next = None
                else:
                    first.next = third
                    second = first.next
                    third = second.next

                continue

            first = first.next
            second = second.next
            third = third.next

        return start_node.next
