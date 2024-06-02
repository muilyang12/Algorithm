# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/


from typing import List


class Solution:
    def insert1(
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

    def insert2(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        added_intervals = intervals[:]
        new_start, _ = newInterval

        for i in range(len(added_intervals)):
            start, _ = added_intervals[i]

            if new_start < start:
                added_intervals.insert(i, newInterval)
                break

        if len(added_intervals) == len(intervals):
            added_intervals.append(newInterval)

        result = [added_intervals[0]]

        for start, end in added_intervals[1:]:
            _, last_end = result[-1]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result


solution = Solution()

print(solution.insert2(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(
    solution.insert2(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    )
)
print(solution.insert2(intervals=[], newInterval=[5, 7]))
