# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


from typing import List


class Solution:
    # Dynamic Programmings
    # time complexity: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        max_profits = [0]

        for i in range(1, len(prices)):
            if prices[i] <= prices[i - 1]:
                continue

            max_profits.append(max_profits[-1] + (prices[i] - prices[i - 1]))

        return max_profits[-1]
