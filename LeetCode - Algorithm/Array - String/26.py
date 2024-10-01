# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        count = 1

        left = 0
        right = 0

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1] = nums[right]

                left = left + 1

                count += 1

        return count


"""
nums = [0,0,1,1,1,2,2,3,3,4]

[0,1,2,3,4,2,2,3,3,4]
"""
