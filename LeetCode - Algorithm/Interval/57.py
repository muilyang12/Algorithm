# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []

        left = 0
        right = 0

        while right < len(intervals):
            if intervals[left][0] > newInterval[1]:
                result.append(newInterval)

                result.extend(intervals[right:])

                break

            elif intervals[left][1] < newInterval[0]:
                result.append(intervals[left])

                left += 1
                right += 1

            elif intervals[right][0] <= newInterval[1]:
                right += 1

            else:
                result.append(
                    [
                        min(intervals[left][0], newInterval[0]),
                        max(intervals[right - 1][1], newInterval[1]),
                    ]
                )

                result.extend(intervals[right:])

                break

        if right == len(intervals):
            if left == len(intervals):
                result.append(newInterval)
            else:
                result.append(
                    [
                        min(intervals[left][0], newInterval[0]),
                        max(intervals[right - 1][1], newInterval[1]),
                    ]
                )

        return result


"""
[[1,3],[6,9]], [2,5]
   ^

[[1,2],[3,5],[6,7],[8,10],[12,16]], [3,8]
   ^

[[1,5]], [2,3]
   ^

[[1,5]], [0,0]
   ^
"""
