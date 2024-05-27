# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/


from typing import List

# [[1,3],[2,6],[8,10],[15,18]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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


solution = Solution()

print(solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge(intervals=[[1, 4], [4, 5]]))
print(solution.merge(intervals=[[5, 10], [1, 5]]))
print(solution.merge(intervals=[[1, 4], [2, 3]]))
