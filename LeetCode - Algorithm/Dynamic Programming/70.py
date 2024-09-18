# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = 1
        memo[1] = 1

        current = 2

        while current < len(memo):
            memo[current] = memo[current - 1] + memo[current - 2]

            current += 1

        return memo[n]
