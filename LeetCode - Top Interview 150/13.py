# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        romanIntMapper = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0

        for index, roman in enumerate(s):
            if roman == "I" and index + 1 < len(s) and s[index + 1] in ["V", "X"]:
                result -= romanIntMapper["I"]
            elif roman == "X" and index + 1 < len(s) and s[index + 1] in ["L", "C"]:
                result -= romanIntMapper["X"]
            elif roman == "C" and index + 1 < len(s) and s[index + 1] in ["D", "M"]:
                result -= romanIntMapper["C"]
            else:
                result += romanIntMapper[roman]

        return result
