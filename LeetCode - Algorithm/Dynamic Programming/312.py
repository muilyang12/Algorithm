# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons/

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = [[0 for _ in nums] for _ in nums]

        for index, num in enumerate(nums):
            dp[index][index] = (
                self.getValue(nums, index - 1) * num * self.getValue(nums, index + 1)
            )

        length = len(nums)

        for diff in range(1, length):
            for left in range(length - diff):
                right = left + diff

                value = -1

                for mid in range(left, right + 1):
                    currentValue = 0

                    if left <= mid - 1:
                        currentValue += dp[left][mid - 1]

                    currentValue += (
                        self.getValue(nums, left - 1)
                        * nums[mid]
                        * self.getValue(nums, right + 1)
                    )

                    if mid + 1 <= right:
                        currentValue += dp[mid + 1][right]

                    value = max(value, currentValue)

                dp[left][right] = value

        return dp[0][length - 1]

    def getValue(self, nums: List[int], index: int) -> int:
        if index < 0 or index > len(nums) - 1:
            return 1

        else:
            return nums[index]


"""
[3,1,5,8]
 ^ ^

[35,16,83,87,84,59,48,41]
 ^  ^        ^
"""

"""
The reason I solved this problem was to implement the "Chained Matrix Multiplication" algorithm, which I 
learned in my Analysis of Algorithms course. In this algorithm, the recurrence relation is 
"M[i][j] = min(k = i to j - 1)(M[i][k] + M[k + 1][j] + p[i - 1] * p[k] * p[j])". To implement this algorithm,
I needed three loops: the first for i, the second for j, and the third for k.

Initially, I incorrectly assumed that I only needed to compare M[i + 1][j] + ___ and M[i][j - 1] + ___ to get
M[i][j]. This was a mistake because the newly multiplied matrix could be placed between i and j.
"""
