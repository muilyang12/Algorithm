# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


import math
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        minimum = math.inf

        while left <= right:
            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])

            if nums[left] <= nums[mid]:
                # Rotated
                if nums[left] >= nums[right]:
                    left = mid + 1
                # Not rotated
                else:
                    right = mid - 1
            else:
                right = mid - 1

        return minimum
