# 15. 3Sum
# https://leetcode.com/problems/3sum/


from typing import List


class Solution:
    # time complexity: O(n^3)
    # Checking membership in a list takes O(n) ('in' operator)
    # Sicing operation takes O(n)
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        result = set()

        length = len(nums)

        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                complement = 0 - (nums[i] + nums[j])

                if not complement in nums[j + 1 :]:
                    continue

                temp_result = tuple(sorted([nums[i], nums[j], complement]))
                result.add(temp_result)

        return list(result)

    # time complexity: O(n^2)
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = set()

        length = len(nums)

        for i in range(length - 2):
            elems_between_i_j = set()

            for j in range(i + 1, length):
                complement = 0 - (nums[i] + nums[j])

                if complement in elems_between_i_j:
                    temp_result = tuple(sorted([nums[i], nums[j], complement]))
                    result.add(temp_result)

                elems_between_i_j.add(nums[j])

        return list(result)

    # time complexity: O(nlogn + n^2) = O(n^2)
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        result = set()

        sorted_nums = sorted(nums)

        length = len(nums)
        for i in range(length - 2):
            left = i + 1
            right = length - 1

            while left < right:
                if sorted_nums[i] + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                elif sorted_nums[i] + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                else:
                    temp_result = tuple(
                        sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    )
                    result.add(temp_result)

                    left += 1
                    right -= 1

        return list(result)


solution = Solution()

print(solution.threeSum2(nums=[-1, 0, 1, 2, -1, -4]))
print(solution.threeSum2(nums=[0, 1, 1]))
print(solution.threeSum2(nums=[0, 0, 0]))
