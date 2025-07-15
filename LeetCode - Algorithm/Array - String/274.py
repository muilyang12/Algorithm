# 274. H-Index
# https://leetcode.com/problems/h-index/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sortedCitations = sorted(citations)

        length = len(citations)
        index = 0
        while length - index > 0:
            if sortedCitations[length - 1 - index] > index:
                index += 1
            else:
                break

        return index


# index = 0
#
# 0, 1, 3, 5, 6
#             ^
