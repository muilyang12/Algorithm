# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted. Right half is not sorted.
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Left half is not sorted. Right half is sorted.
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# 1,2,4,5,6,7,0
# l     m     r

# 4,5,6,7,0,1,2
# l     m     r

# 6,7,0,1,2,4,5
# l     m     r

# 0,1,2,4,5,6,7
# l     m     r
