# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/


from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        new_start, _ = newInterval

        result = intervals[:]

        isInserted = False
        for i in range(len(result)):
            start, _ = result[i]

            if start < new_start:
                continue

            else:
                result.insert(i, newInterval)
                isInserted = True
                break

        if not isInserted:
            result.append(newInterval)

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

print(solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(
    solution.insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    )
)
print(solution.insert(intervals=[], newInterval=[5, 7]))
