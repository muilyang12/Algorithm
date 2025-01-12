# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}

        for num in arr:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        counts = list(occurrences.values())
        countsSet = set(counts)

        return len(counts) == len(countsSet)
