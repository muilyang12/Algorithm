# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]

        for i in range(2, len(cost)):
            memo[i] = min(memo[i - 2] + cost[i], memo[i - 1] + cost[i])

        return min(memo[-1], memo[-2])


"""
cost = [1,100,1,1,1,100,1,1,100,1]

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
