# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/


from typing import List
import math


class Solution:
    # Sliding Window
    # time complexity: O(n ^ 2)
    # Time Limit Exceeded :(
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0

        result = math.inf

        while right < len(nums):
            targetNums = nums[left : right + 1]
            currentSum = sum(targetNums)

            if currentSum == target:
                result = min(result, right - left + 1)
                left += 1

            elif currentSum > target:
                result = min(result, right - left + 1)
                left += 1

            else:
                right += 1

        return result if result != math.inf else 0

    # Sliding Window
    # time complexity: O(n)
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0

        result = math.inf

        currentSum = nums[0]

        while right < len(nums):
            if currentSum >= target:
                result = min(result, right - left + 1)
                currentSum -= nums[left]
                left += 1

            else:
                right += 1
                if right < len(nums):
                    currentSum += nums[right]

        return result if result != math.inf else 0
