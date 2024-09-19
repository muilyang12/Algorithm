# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)

        current = 1

        while current < len(memo):
            for i in range(current):
                if nums[current] > nums[i]:
                    memo[current] = max(memo[current], memo[i] + 1)

            current += 1

        return max(memo)
