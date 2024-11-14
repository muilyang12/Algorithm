# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


class Solution:
    def __init__(self):
        self.vowels = set(["a", "e", "i", "o", "u"])

    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        current = 0

        left = 0
        right = k - 1

        for i in range(left, right + 1):
            if s[i] in self.vowels:
                current += 1

        result = max(result, current)

        left += 1
        right += 1

        while right < len(s):
            if s[left - 1] in self.vowels:
                current -= 1
            if s[right] in self.vowels:
                current += 1

            result = max(result, current)

            left += 1
            right += 1

        return result
