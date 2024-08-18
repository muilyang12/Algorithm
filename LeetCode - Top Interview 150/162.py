# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            elif mid + 1 <= len(nums) - 1 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                return mid

        return 0
