# 15. 3Sum
# https://leetcode.com/problems/3sum/


from typing import List


class Solution:
    # time complexity: O(n^3)
    # Checking membership in a list takes O(n) ('in' operator)
    # Sicing operation takes O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        length = len(nums)

        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                complement = 0 - (nums[i] + nums[j])

                if not complement in nums[j + 1 :]:
                    continue

                temp_result = tuple(sorted([nums[i], nums[j], complement]))

                if temp_result in result:
                    continue

                result.add(temp_result)

        return list(result)
