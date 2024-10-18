# 540. Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid % 2 == 1:
                if nums[mid - 1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return nums[left]


"""
In this question, the problem explicitly states that the algorithm must run in O(log n) time, making it 
straightforward to think of using a binary search. However, in most cases, there won't be such a clear hint, 
so I need to recognize when to apply binary search on my own.

I believe the key condition is when the problem asks me to find one specific element. If I need to select
two points to satisfy a certain condition or calculate a value within a range, I would use approaches like
two pointers or sliding windows. But when I'm tasked with finding a single element that meets specific 
condition, it's very likely a binary search problem.
"""
