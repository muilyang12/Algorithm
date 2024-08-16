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
