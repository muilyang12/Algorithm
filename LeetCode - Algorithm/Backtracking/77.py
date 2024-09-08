# 77. Combinations
# https://leetcode.com/problems/combinations/


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        self.makeCombinationList(n, k, 1, [], result)

        return result

    def makeCombinationList(
        self, n: int, k: int, start: int, current: List[int], result: List[List[int]]
    ):
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, n - (k - len(current)) + 2):
            current.append(i)
            self.makeCombinationList(n, k, i + 1, current, result)
            current.pop()
