# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndexMapper = {num: index for index, num in enumerate(nums)}

        for index, num in enumerate(nums):
            complement = target - num

            if not complement in numIndexMapper:
                continue

            if index == numIndexMapper[complement]:
                continue

            return [index, numIndexMapper[complement]]

        return []
