# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

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


"""
If I encountered this question without any guidance, it would be really hard to realize that I need to use 
binary search. :(

In this problem, I need to find one specific value, and that value should be between 1 and the largest value 
in the array. This is very similar to the kind of problem where I have to pick one element out of an array. 
As I mentioned earlier in another LeetCode question, the biggest hint that binary search is needed comes from 
the fact that I have to pick one element from a range. So here, I must use binary search!
"""
