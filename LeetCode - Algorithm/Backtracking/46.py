# 46. Permutations
# https://leetcode.com/problems/permutations/


from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.makePermutationList(nums, [], result)

        return result

    def makePermutationList(self, nums: int, used: List[int], result: List[int]):
        for num in nums:
            if num in used:
                continue

            used.append(num)

            if len(used) == len(nums):
                result.append(list(used))
            else:
                self.makePermutationList(nums, used, result)

            used.remove(num)
