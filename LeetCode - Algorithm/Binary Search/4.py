# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    # Did not finish solving it. :(
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return (
                nums2[len(nums2) // 2]
                if len(nums2) % 2 == 1
                else (nums2[len(nums2) / 2] + nums2[len(nums2) / 2 - 1]) / 2
            )

        if len(nums2) == 0:
            return (
                nums1[len(nums1) // 2]
                if len(nums1) % 2 == 1
                else (nums1[len(nums1) / 2] + nums1[len(nums1) / 2 - 1]) / 2
            )

        sumOfMids = (len(nums1) + len(nums2)) // 2 - 1

        left1 = 0
        right1 = len(nums1) - 1

        while True:
            mid1 = (left1 + right1) // 2
            mid2 = sumOfMids - mid1

            if len(nums2) > mid2 + 1 and nums1[mid1] > nums2[mid2 + 1]:
                right1 = mid1 - 1

            elif len(nums1) > mid1 + 1 and nums1[mid1 + 1] < nums2[mid2]:
                left1 = mid1 + 1

            else:
                break

        return (
            (nums1[mid1] + nums2[mid2]) / 2
            if (len(nums1) + len(nums2)) % 2 == 0
            else max(nums1[mid1], nums2[mid2])
        )


"""
nums1 = [-1,0,1,3,5,7], nums2 = [2,4]
                ^                ^
nums1 = [-1,1,3,5,7], nums2 = [0,2,4]
              ^                  ^
nums1 = [1,3,5,7], nums2 = [-1,0,2,4]
           ^                     ^
nums1 = [1,3,5,7], nums2 = [0,2,4]
           ^                  ^
nums1 = [1,3], nums2 = [2]
         ^              ^
nums1 = [3], nums2 = [-2,-1]
         ^            ^

-1,0,1,2,3,4,5,7 -> median = 2.5
0,1,2,3,4,5,7 -> median = 3
1,2,3 -> median = 2
-2,-1,3 -> median = -1

"""
