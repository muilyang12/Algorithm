# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0

        current = 0
        currentNum = None
        currentCount = None

        destination = None

        while current < len(nums):
            num = nums[current]

            if currentNum == None or num != currentNum:
                result += 1

                currentNum = num
                currentCount = 1

                current += 1

                if destination:
                    nums[destination] = num

                    destination += 1

            elif num == currentNum and currentCount < 2:
                result += 1

                currentCount += 1

                current += 1

                if destination:
                    nums[destination] = num

                    destination += 1

            elif num == currentNum and currentCount == 2:
                if not destination:
                    destination = current

                current += 1

        return result


"""
[0,0,0,0,1,1,1,1,2,3,3]
                     ^
des = 7

[0,0,1,1,2,3,3,1,2,3,3]
"""
