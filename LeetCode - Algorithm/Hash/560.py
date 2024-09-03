# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List
from collections import defaultdict


class Solution:
    # I tried to use the sliding window method to solve this problem, but it doesn't work here because
    # the constraint allows negative integers to be included in the nums array. It feels like there
    # should be a constraint to include only positive numbers to effectively use the sliding window method.
    def subarraySum1(self, nums: List[int], k: int) -> int:
        result = 0

        def calculateSum(nums, left, right):
            sum = 0

            for i in range(left, right + 1):
                sum += nums[i]

            return sum

        for i in range(len(nums)):
            left = i
            right = i

            currentSum = calculateSum(nums, left, right)

            while currentSum < k:
                right += 1

                if right >= len(nums):
                    break

                currentSum = calculateSum(nums, left, right)

            if currentSum == k:
                result += 1

        return result

    def subarraySum2(self, nums: List[int], k: int) -> int:
        hash = defaultdict(int)
        hash[0] = 1

        result = 0

        cumulated = 0
        for num in nums:
            cumulated += num

            if cumulated - k in hash:
                result += hash[cumulated - k]

            hash[cumulated] += 1

        return result
