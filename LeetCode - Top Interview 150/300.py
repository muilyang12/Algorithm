# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)

        memo = [1 for _ in range(length)]

        for i in range(1, length):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue

                memo[i] = max(memo[i], memo[j] + 1)

        return max(memo)
