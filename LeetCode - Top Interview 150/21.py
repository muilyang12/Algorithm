# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list1_ptr = list1
        list2_ptr = list2

        dummy = current = ListNode()

        while list1_ptr or list2_ptr:
            if list1_ptr and not list2_ptr:
                current.next = list1_ptr
                list1_ptr = list1_ptr.next

            elif not list1_ptr and list2_ptr:
                current.next = list2_ptr
                list2_ptr = list2_ptr.next

            elif list1_ptr.val < list2_ptr.val:
                current.next = list1_ptr
                list1_ptr = list1_ptr.next

            else:
                current.next = list2_ptr
                list2_ptr = list2_ptr.next

            current = current.next

        return dummy.next
