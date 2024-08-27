# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from typing import List


class Solution:
    # Sliding Window
    # time complexity: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        left = 0
        right = 1

        maximumProfit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                maximumProfit = max(maximumProfit, prices[right] - prices[left])

            right += 1

        return maximumProfit
