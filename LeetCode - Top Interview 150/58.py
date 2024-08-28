# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        splitted = re.split(r"\s+", s)

        return len(splitted[-1])


"""
The 're' module in Python

1. re.match
re.match(r'fly', 'fly me to the moon or fly me to the mars.')

2. re.search
re.search(r'fly', 'fly me to the moon or fly me to the mars.')

3. re.findall
- Finds all occurrences of a pattern in the string
re.findall(r'fly', 'fly me to the moon or fly me to the mars.')

3. re.sub
re.match(r'/s+', ' ', 'fly   me to     the   moon.')

4. re.split
re.split(r'/s+', ' ', 'fly   me to     the   moon.')

"""
