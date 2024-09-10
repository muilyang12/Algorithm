# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import List


class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        leftEnd = self.searchTheMostRight1(nums, target - 1) + 1
        rightEnd = self.searchTheMostRight1(nums, target)

        return (
            [leftEnd, rightEnd]
            if leftEnd < len(nums) and nums[leftEnd] == target
            else [-1, -1]
        )

    def searchTheMostRight1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        leftEnd = self.searchTheMostLeft2(nums, target)
        rightEnd = self.searchTheMostRight2(nums, target)

        return [leftEnd, rightEnd]

    def searchTheMostLeft2(self, nums: List[int], target: int) -> int:
        index = -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                index = mid
                right = mid - 1

        return index

    def searchTheMostRight2(self, nums: List[int], target: int) -> int:
        index = -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                index = mid
                left = mid + 1

        return index
