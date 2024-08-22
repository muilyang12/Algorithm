# 169. Majority Element
# https://leetcode.com/problems/majority-element/


from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = defaultdict(int)

        for num in nums:
            hash[num] += 1

            if hash[num] > len(nums) // 2:
                return num
