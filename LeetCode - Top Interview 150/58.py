# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        splitted = re.split(r"\s+", s)

        return len(splitted[-1])

