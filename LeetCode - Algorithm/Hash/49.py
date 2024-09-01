# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)


"""
Requirements for Keys in dict and defaultdict
- Immutable
- Hashable

Examples of Valid Keys:
- Integers: 1, 2, 3
- Floats: 3.14, 2.71
- Strings: "apple", "banana", "cherry"
- Tuples: ("a", 1), (3.14, "pi")
- Booleans: True, False
- NoneType: None

Examples of Invalid Keys:
- Lists: [1, 2, 3]
- Dictionaries: {"key": "value"}
- Sets: {1, 2, 3}

-> The code below doesn't work because list type is not a valid key in the dictionary.

   hash = default(list)
   data = [1, 2, 3]

   hash[data].append("123")
"""
