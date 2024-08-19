# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/


from typing import List


class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
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

    def findPeakElement2(self, nums: List[int]) -> int:
        def find_peak(left, right):
            if right - left == 1:
                return left

            mid = (left + right) // 2

            left_peak_index = find_peak(left, mid)
            right_peak_index = find_peak(mid, right)

            return (
                left_peak_index
                if nums[left_peak_index] >= nums[right_peak_index]
                else right_peak_index
            )

        return find_peak(0, len(nums))
