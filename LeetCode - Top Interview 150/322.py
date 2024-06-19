# 322. Coin Change
# https://leetcode.com/problems/coin-change/


from typing import List


class Solution:
    # 무언가 누적이라는 느낌이 들면 DP를 사용해야할 것 같네.
    # time complexity: O(n)
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins_for_change = [99999 for i in range(amount + 1)]
        num_coins_for_change[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue

                num_coins_for_change[i] = min(
                    num_coins_for_change[i], num_coins_for_change[i - coin] + 1
                )

        return num_coins_for_change[-1] if num_coins_for_change[-1] != 99999 else -1
