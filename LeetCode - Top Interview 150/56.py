# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/


from typing import List


class Solution:
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        result = sorted(intervals, key=lambda x: x[0])

        left = 0
        right = 1

        while True:
            if right >= len(result):
                break

            left_start, left_end = result[left]
            right_start, right_end = result[right]

            if left_end < right_start:
                left += 1
                right += 1

            else:
                result[left] = [left_start, max(left_end, right_end)]

                del result[right]

        return result

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        result = [sorted_intervals[0]]

        for start, end in sorted_intervals[1:]:
            _, last_end = result[-1]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result


solution = Solution()

print(solution.merge2(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge2(intervals=[[1, 4], [4, 5]]))
print(solution.merge2(intervals=[[5, 10], [1, 5]]))
print(solution.merge2(intervals=[[1, 4], [2, 3]]))
