# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/


from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        count_without_cycle = k % len(nums)

        for _ in range(count_without_cycle):
            popped = nums.pop()
            nums.insert(0, popped)

    def rotate2(self, nums: List[int], k: int) -> None:
        count_without_cycle = k % len(nums)
        index_for_slicing = -1 * count_without_cycle

        nums[:] = nums[index_for_slicing:] + nums[:index_for_slicing]
