# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        memo = [num for num in nums]

        for i in range(1, len(nums)):
            memo[i] = max(memo[i], memo[i - 1] + nums[i])

        return max(memo)

    def maxSubArray2(self, nums: List[int]) -> int:
        currentMax = globalMax = nums[0]

        for i in range(1, len(nums)):
            currentMax = max(currentMax + nums[i], nums[i])
            globalMax = max(globalMax, currentMax)

        return globalMax


"""
nums = [-2,1,-3,4,-1,2,1,-5,4]
                            ^
memo = [0,0,1,0,4,3,5,6,1,5]
                          ^
"""
