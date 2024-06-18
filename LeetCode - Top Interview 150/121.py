# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from typing import List


class Solution:
    # time complexity: O(n ^ 2)
    def maxProfit1(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices) - 1):
            buying_price = prices[i]
            selling_price = max(prices[i + 1 :])

            max_profit = max(max_profit, selling_price - buying_price)

        return max_profit

    # time complexity: O(n)
    def maxProfit2(self, prices: List[int]) -> int:
        buying_price = prices[0]
        max_profit = 0

        for price in prices:
            buying_price = min(buying_price, price)
            max_profit = max(max_profit, price - buying_price)

        return max_profit
