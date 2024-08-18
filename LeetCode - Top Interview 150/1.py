# 1. Two Sum
# https://leetcode.com/problems/two-sum/


from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num], i]

            hash[num] = i

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
