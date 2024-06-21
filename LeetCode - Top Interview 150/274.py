# 274. H-Index
# https://leetcode.com/problems/h-index/


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations)
        length = len(sorted_citations)

        h_index = 0
        for i in range(1, length + 1):
            if i > length:
                break

            if sorted_citations[-i] >= i:
                h_index = i

                continue

        return h_index


solution = Solution()

print(solution.hIndex(citations=[3, 0, 6, 1, 5]))
print(solution.hIndex(citations=[1, 3, 1]))
print(solution.hIndex(citations=[1]))
print(solution.hIndex(citations=[100]))
