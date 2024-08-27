# 1423. Maximum Points You Can Obtain from Cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


from typing import List


class Solution:
    # Sliding Window
    # time complexity: O(n)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - 1 - k

        result = 0

        currentSum = sum(cardPoints[len(cardPoints) - 1 - k + 1 :])

        while right < len(cardPoints):
            result = max(result, currentSum)

            if left < len(cardPoints):
                currentSum += cardPoints[left]
            if right + 1 < len(cardPoints):
                currentSum -= cardPoints[right + 1]

            left += 1
            right += 1

        return result
