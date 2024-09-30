# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        result = [intervals[0]]

        i = 1
        j = 0

        while i < len(intervals):
            targetBeginning = intervals[i][0]
            resultEnd = result[j][1]

            if targetBeginning <= resultEnd:
                result[j][1] = max(result[j][1], intervals[i][1])
                i += 1
            else:
                result.append(intervals[i])
                i += 1
                j += 1

        return result


"""
[[1,3],[2,6],[8,10],[15,18]]
               ^
[[1,3]]
   ^
"""
