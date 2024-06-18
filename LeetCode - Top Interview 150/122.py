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

    def maxProfit2(self, prices: List[int]) -> int:
        def prevMaxProfit(self, prices: List[int]) -> int:
            buying_price = prices[0]
            max_profit = 0

            for price in prices:
                buying_price = min(buying_price, price)
                max_profit = max(max_profit, price - buying_price)

            return max_profit

        max_profit = 0

        left = 0
        right = 1

        while left < len(prices):
            if right >= len(prices):
                left += 1
                right = left + 1

            if prices[right] > prices[left]:
                max_profit += prices[right] - prices[left]

                left = right
                right = right + 1

                print(left, right, prices[right] - prices[left], max_profit)

            else:
                right += 1

        return max_profit
