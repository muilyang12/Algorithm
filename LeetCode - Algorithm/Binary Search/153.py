# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid == 0 and nums[mid] <= nums[-1]:
                return nums[mid]

            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            # Left half is sorted. Right half is not sorted.
            if nums[left] <= nums[mid]:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    left = mid + 1

            # Left half is not sorted. Right half is sorted.
            else:
                right = mid - 1


# 1,2,4,5,6,7,0
# l     m     r

# 4,5,6,7,0,1,2
# l     m     r

# 6,7,0,1,2,4,5
# l     m     r

# 0,1,2,4,5,6,7
# l     m     r
