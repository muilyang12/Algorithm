# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/


from typing import List
from collections import defaultdict


class Solution:
    # Sliding Window
    # time complexity: O(n * m)
    # Time Limit Exceeded :(
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        left = 0
        right = len(p) - 1

        result = []

        countOfLettersInP = defaultdict(int)
        for letter in p:
            countOfLettersInP[letter] += 1

        while right < len(s):
            currentWindowCountOfLetters = defaultdict(int)
            for letter in s[left : right + 1]:
                currentWindowCountOfLetters[letter] += 1

            for i in range(len(p)):
                targetLetter = p[i]
                if (
                    countOfLettersInP[targetLetter]
                    != currentWindowCountOfLetters[targetLetter]
                ):
                    break

                if i == len(p) - 1:
                    result.append(left)

            left += 1
            right += 1

        return result

    # Sliding Window
    # time complexity: O(n * m)
    # It's fascinating how the current window's sum or letter count is calculated by
    # adding and removing elements one by one as the window shifts.
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        left = 0
        right = len(p) - 1

        result = []

        countOfLettersInP = defaultdict(int)
        for letter in p:
            countOfLettersInP[letter] += 1

        currentWindowCountOfLetters = defaultdict(int)
        for letter in s[left : right + 1]:
            currentWindowCountOfLetters[letter] += 1

        while right < len(s):
            if self.areDictsSame(currentWindowCountOfLetters, countOfLettersInP):
                result.append(left)

            currentWindowCountOfLetters[s[left]] -= 1
            if right + 1 < len(s):
                currentWindowCountOfLetters[s[right + 1]] += 1

            left += 1
            right += 1

        return result

    def areDictsSame(self, first, second) -> bool:
        secondLength = len(second)

        for letter in second:
            if first[letter] == second[letter]:
                secondLength -= 1

        if secondLength == 0:
            return True
        else:
            return False
