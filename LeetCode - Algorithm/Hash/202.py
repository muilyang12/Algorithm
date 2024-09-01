# 202. Happy Number
# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        currentNumber = n

        while not currentNumber in visited:
            visited.add(currentNumber)

            currentNumber = self.getSumOfDigitSquare(currentNumber)

            if currentNumber == 1:
                return True

        return False

    def getSumOfDigitSquare(self, number: int) -> int:
        result = 0

        for digit in str(number):
            result += int(digit) ** 2

        return result
