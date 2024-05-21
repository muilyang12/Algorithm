# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict


class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet_counter01 = defaultdict(int)
        alphabet_counter02 = defaultdict(int)

        for alphabet01 in s:
            alphabet_counter01[alphabet01] += 1

        for alphabet02 in t:
            alphabet_counter02[alphabet02] += 1

        for alphabet in alphabet_counter01:
            if alphabet_counter01[alphabet] != alphabet_counter02[alphabet]:
                return False

        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet_counter = defaultdict(int)

        for alphabet in s:
            alphabet_counter[alphabet] += 1

        for alphabet in t:
            alphabet_counter[alphabet] -= 1

        for value in alphabet_counter.values():
            if value != 0:
                return False

        return True
