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

    def permute2(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.makePermutationList2(nums, [], [False] * len(nums), result)

        return result

    def makePermutationList2(
        self, nums: int, path: List[int], visited: List[bool], result: List[int]
    ):
        for index, num in enumerate(nums):
            if visited[index]:
                continue

            path.append(num)
            visited[index] = True

            if len(path) == len(nums):
                result.append(list(path))
            else:
                self.makePermutationList2(nums, path, visited, result)

            path.remove(num)
            visited[index] = False


"""
In my previous solution, I checked at each step of the loop whether a new number already existed in the current 'path'. 
Realizing this was inefficient, I decided to use a set for the 'path' to speed up the checking process. Then, I converted 
the 'path' back to a list just before adding it to the result. However it did not work.

The new method introduces an additional argument called 'visited,' which is initialized as a list of False values with 
a length equal to len(nums). Each time a new value is added to the path, the corresponding index in the ' visited' array
is set to True. This way, we no longer need to check if a specific value exists in the 'path'. Instead, we only need to
verify whether the value in the 'visited' array is False.

Realizing that checking for the existence of a number in every loop was inefficient was a great insight. The approach using
a set was a good attempt, but I need to remember the 'visited' array method going forward.
"""
