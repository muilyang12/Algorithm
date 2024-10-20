# 1011. Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/search-insert-position/

from typing import List
import math


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            numDays = 1
            currentWeight = 0

            current = 0

            while current < len(weights):
                if weights[current] > mid:
                    numDays = math.inf
                    break

                if currentWeight + weights[current] > mid:
                    numDays += 1
                    currentWeight = 0
                else:
                    currentWeight += weights[current]
                    current += 1

            if numDays <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left


"""
[1,2,3,4,5,6,7,8,9,10]
"""
