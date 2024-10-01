# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        sArray = s.split()

        result = ""

        current = len(sArray) - 1

        while current >= 0:
            result += sArray[current]

            if current > 0:
                result += " "

            current -= 1

        return result
