# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)

        left = 1
        right = piles[-1]

        while left <= right:
            mid = (left + right) // 2

            dividedPiles = list(
                map(lambda x: x // mid if x % mid == 0 else x // mid + 1, piles)
            )

            if sum(dividedPiles) <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left
