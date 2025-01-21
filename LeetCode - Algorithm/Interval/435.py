# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        sortedIntervals = sorted(intervals, key=lambda x: x[0])

        result = 0

        prev = 0
        curr = 1

        while curr < len(intervals):
            start1, end1 = sortedIntervals[prev]
            start2, end2 = sortedIntervals[curr]

            if start2 < end1:
                result += 1

                if end1 <= end2:
                    prev = prev
                else:
                    prev = curr
            else:
                prev = curr

            curr += 1

        return result


# start1 < end2 and start2 < end1 -> This condition is straightforward for determining whether there is an overlap.
