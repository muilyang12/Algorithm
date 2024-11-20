# 2215. Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)

        for num1 in nums1:
            if num1 in nums2Set:
                nums1Set.remove(num1)
                nums2Set.remove(num1)

        return [list(nums1Set), list(nums2Set)]
