# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/

from typing import List


class Solution:
    # time complexity: O(n ^ 2)
    # Time Limit Exceeded :(
    def longestOnes1(self, nums: List[int], k: int) -> int:
        result = 0

        left = 0
        right = 0

        count = 0

        for left in range(len(nums)):
            tempResult = 0

            right = left

            while count <= k and right < len(nums):
                if nums[right] == 1:
                    right += 1
                    tempResult += 1

                else:
                    if count == k:
                        break

                    count += 1

                    right += 1
                    tempResult += 1

            result = max(result, tempResult)

            count = 0

        return result


# nums = [1,1,1,0,0,0,1,1,1,1,0]
#               ^ ^
