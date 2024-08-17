# 148. Sort List
# https://leetcode.com/problems/sort-list/


from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head

        left = head
        node_before_right = self.get_mid(head)
        right = node_before_right.next
        node_before_right.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        dummy = ListNode(-1)
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left

                left = left.next
                current = current.next

            else:
                current.next = right

                right = right.next
                current = current.next

        if left:
            current.next = left

        if right:
            current.next = right

        return dummy.next

    # This approach looks awesome!
    def get_mid(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Basic Merge Sort
    # time complexity: O(nlogn)
    def basic_merge_sort(self, arr: List[int]):
        if len(arr) <= 1:
            return

        # Divide
        left_array = arr[: len(arr) // 2]
        right_array = arr[len(arr) // 2 :]

        self.basic_merge_sort(left_array)
        self.basic_merge_sort(right_array)

        # Merge
        i = 0
        j = 0
        k = 0  # Merged list index

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
                k += 1

            else:
                arr[k] = right_array[j]
                j += 1
                k += 1

        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1


solution = Solution()

initial_array = [2, 3, 5, 1, 7, 4, 4, 6, 0]
print(initial_array)
solution.basic_merge_sort(initial_array)
print(initial_array)
