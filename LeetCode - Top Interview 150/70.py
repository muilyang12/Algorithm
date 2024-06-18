# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/


from typing import List


class Solution:
    # 무언가 누적이라는 느낌이 들면 DP를 사용해야할 것 같네.
    # time complexity: O(n)
    def climbStairs(self, n: int) -> int:
        ways = [1, 2]

        for i in range(2, n):
            ways.append((ways[i - 2]) + (ways[i - 1]))

        return ways[n - 1]
