# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    # This approach obviously has a time complexity of O(n^2)
    def longestConsecutive1(self, nums: List[int]) -> int:
        numsSet = set(nums)

        result = 0

        for num in numsSet:
            target = num
            currentResult = 1

            while target + 1 in numsSet:
                currentResult += 1
                target += 1

            result = max(result, currentResult)

        return result

    # To improve it, I brought a new approach that uses a hash map to reduce the number
    # of recursive calls, but it still results in O(n^2) time complexity
    def longestConsecutive2(self, nums: List[int]) -> int:
        numsSet = set(nums)
        hash = {}

        result = 0

        for num in numsSet:
            target = num
            currentResult = 1

            while target + 1 in numsSet:
                if target + 1 in hash:
                    currentResult += hash[target + 1]
                    break

                currentResult += 1
                target += 1

            hash[num] = currentResult

            result = max(result, currentResult)

        return result

    # By excluding elements that are not the start of a consecutive sequence, this final
    # approach achieves a time complexity of O(n).
    def longestConsecutive3(self, nums: List[int]) -> int:
        numsSet = set(nums)

        result = 0

        for num in numsSet:
            if num - 1 in numsSet:
                continue

            target = num
            currentResult = 1

            while target + 1 in numsSet:
                currentResult += 1
                target += 1

            result = max(result, currentResult)

        return result
