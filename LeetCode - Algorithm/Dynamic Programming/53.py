# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        memo[0] = nums[0]

        for i in range(1, len(nums)):
            memo[i] = max(memo[i - 1] + nums[i], nums[i])

        return max(memo)


"""
nums = [-2,1,-3,4,-1,2,1,-5,4]
                            ^
memo = [0,0,1,0,4,3,5,6,1,5]
                          ^
"""
