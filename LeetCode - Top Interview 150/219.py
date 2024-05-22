# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/


from typing import List


class Solution:
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        left = 0
        right = left + 1

        for i in range(len(nums) - 1):
            left = i

            for j in range(1, k + 1):
                right = left + j

                if right >= len(nums):
                    break

                if nums[left] == nums[right]:
                    return True

        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        hash_map = {}

        for i in range(len(nums)):
            if not nums[i] in hash_map:
                hash_map[nums[i]] = i

                continue

            if abs(hash_map[nums[i]] - i) <= k:
                return True

            else:
                hash_map[nums[i]] = i

        return False


solution = Solution()

print(solution.containsNearbyDuplicate1(nums=[1, 2, 3, 1], k=3))
print(solution.containsNearbyDuplicate1(nums=[1, 0, 1, 1], k=1))
print(solution.containsNearbyDuplicate1(nums=[1, 2, 3, 1, 2, 3], k=2))
print(solution.containsNearbyDuplicate1(nums=[99, 99], k=2))
