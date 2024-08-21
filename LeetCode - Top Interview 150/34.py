# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        found_mid = -1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                found_mid = mid

                break

        if found_mid == -1:
            return [-1, -1]

        result = [-1, -1]

        left = 0
        right = found_mid - 1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

                result[0] = mid

        left = found_mid + 1
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

                result[1] = mid

        if found_mid != -1:
            result[0] = found_mid if result[0] == -1 else result[0]
            result[1] = found_mid if result[1] == -1 else result[1]

        return result
