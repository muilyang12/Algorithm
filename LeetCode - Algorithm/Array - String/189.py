# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        actualNumRotation = k % len(nums)

        index = len(nums) - 1

        tempNums = []

        for _ in range(actualNumRotation):
            tempNums.append(nums[index])
            index -= 1

        while index >= 0:
            nums[index + actualNumRotation] = nums[index]
            index -= 1

        for i in range(actualNumRotation):
            nums[actualNumRotation - 1 - i] = tempNums[i]
