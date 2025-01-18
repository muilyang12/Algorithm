# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0

        while right < len(nums):
            if left == right and nums[left] == 0:
                right += 1

            elif left == right and nums[right] != 0:
                left += 1
                right += 1

            elif nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right += 1

            else:
                right += 1


# nums = [0,1,0,3,12]
#         ^ ^
# nums = [1,0,0,3,12]
#           ^ ^
#           ^   ^
# nums = [1,3,0,0,12]
#             ^   ^
# nums = [1,3,12,0,0]
#                ^   ^
