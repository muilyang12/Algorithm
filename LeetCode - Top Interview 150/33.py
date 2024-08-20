# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/


from typing import List

"""
target: 6
0, 6 -> mid: 3
[1,2,4,5,6,7,0] 5
[6,7,0,1,2,4,5] 1
[4,5,6,7,0,1,2] 7

target: 8
[4,5,6,7,8,1,2,3]
0, 7, 3 -> 7
"""


class Solution:
    # target 0
    # [6,7,0,1,2,4,5] 1
    # target 5
    # [2,4,5,6,7,0,1] 6
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if target > nums[mid]:
                    left = mid + 1
                elif nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if target < nums[mid]:
                    right = mid - 1
                elif nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                if target < nums[left]:
                    left = mid + 1
                elif target > nums[left]:
                    right = mid - 1
                else:
                    return left
            elif target > nums[mid]:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                elif nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    return right
            else:
                return mid

        return -1
