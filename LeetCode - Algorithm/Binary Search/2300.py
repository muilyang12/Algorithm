# 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from typing import List


class Solution:
    def successfulPairs1(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        result = []

        for spell in spells:
            current = 0

            for potion in potions:
                if spell * potion >= success:
                    current += 1

            result.append(current)

        return result

    def successfulPairs2(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        result = []

        sortedPotions = sorted(potions)

        print(sortedPotions)

        for spell in spells:
            left = 0
            right = len(potions) - 1

            while left <= right:
                mid = (left + right) // 2

                if spell * sortedPotions[mid] < success:
                    left = mid + 1
                elif spell * sortedPotions[mid] >= success:
                    right = mid - 1

            result.append(len(potions) - left)

        return result


"""
spells = [40,11,24,28,40,22,26,38,28,10,31,16,10,37,13,21,9,22,21,18,34,2,40,40,6,16,9,14,14,15,37,15,32,4,27,20,24,12,26,39,32,39,20,19,22,33,2,22,9,18,12,5]
potions = [31,40,29,19,27,16,25,8,33,25,36,21,7,27,40,24,18,26,32,25,22,21,38,22,37,34,15,36,21,22,37,14,31,20,36,27,28,32,21,26,33,37,27,39,19,36,20,23,25,39,40]

[7, 8, 14, 15, 16, 18, 19, 19, 20, 20, 21, 21, 21, 21, 22, 22, 22, 23, 24, 25, 25, 25, 25, 26, 26, 27, 27, 27, 27, 28, 29, 31, 31, 32, 32, 33, 33, 34, 36, 36, 36, 36, 37, 37, 37, 38, 39, 39, 40, 40, 40]
                                                                           ^       ^           ^
"""
