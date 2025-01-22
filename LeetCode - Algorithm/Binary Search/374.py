# 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/


def guess(num: int) -> int:
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            target = (left + right) // 2

            if guess(target) == -1:
                right = target - 1
            elif guess(target) == 1:
                left = target + 1
            else:
                return target
