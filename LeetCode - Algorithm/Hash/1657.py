# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

from typing import Dict
from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        charsCounts1 = self.getCharsCounts(word1)
        charsCounts2 = self.getCharsCounts(word2)

        chars1 = sorted(charsCounts1.keys())
        chars2 = sorted(charsCounts2.keys())

        for char1, char2 in zip(chars1, chars2):
            if char1 != char2:
                return False

        counts1 = sorted(charsCounts1.values())
        counts2 = sorted(charsCounts2.values())

        for count1, count2 in zip(counts1, counts2):
            if count1 != count2:
                return False

        return True

    def getCharsCounts(self, word: str) -> Dict[str, int]:
        counts = defaultdict(int)

        for char in word:
            counts[char] += 1

        return counts
