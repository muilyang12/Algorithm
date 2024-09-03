# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        result = 0

        target = None

        for num in nums:
            if num - 1 in nums_set:
                continue

            current_result = 1

            target = num
            while target + 1 in nums_set:
                current_result += 1

                target += 1

            result = max(result, current_result)

        return result


solution = Solution()

print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
