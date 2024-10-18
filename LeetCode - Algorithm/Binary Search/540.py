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
