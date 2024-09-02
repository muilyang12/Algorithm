# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/


from typing import List


class Solution:
    # time complexity: O(nlogn + n^2) = O(n^2)
    # Deleting an element from a list in Python is an O(n) operation
    # because it involves shifting all subsequent elements one position to the left.
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

    # time complexity: O(nlogn + n) = O(nlogn)
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

"""
===== Knowledge =====

- Definition
Lambda Expression is a way to create small, anonymous functions.

- Example of a Lambda Expression
add = lambda x, y: x + y
result = add(2, 3) -> 5

- Example of Using Lambda Expressions with Higher-Order Functions
Lambda expressions are particularly useful when combined with higher-order functions, which are functions that take other functions as arguments.

1. 
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers) -> 15

2.
numbers = [1, 2, 3, 4, 5]
odd_numbers = filter(lambda x: x % 2 == 1, numbers) -> [1, 3, 5]

3.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers)) -> [1, 4, 9, 16, 25]

4.
names = ["Yoonseok", "Junho", "Kim", "Muil"]
sorted_names = sorted(names, key=lambda x: len(x))
  -> ["Kim", "Muil", "Junho", "Yoonseok"]
"""
