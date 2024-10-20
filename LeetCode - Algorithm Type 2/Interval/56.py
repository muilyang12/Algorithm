from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        result = []
        result.append(intervals[0])

        current = 1

        while current < len(intervals):
            resultStart, resultEnd = result[-1]
            currentStart, currentEnd = intervals[current]

            if currentStart <= resultEnd:
                result[-1][0] = min(resultStart, currentStart)
                result[-1][1] = max(resultEnd, currentEnd)
            else:
                result.append(intervals[current])

            current += 1

        return result
