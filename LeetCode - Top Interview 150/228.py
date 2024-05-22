# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/


from typing import List


class Solution:
    def summaryRanges1(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [f"{nums[0]}"]

        result = []

        left = 0
        right = 1

        while right <= len(nums):
            start_num = nums[left]
            end_num = -1

            while right < len(nums) and nums[left] + 1 == nums[right]:
                left += 1
                right += 1

            end_num = nums[left]

            left = right
            right = left + 1

            if end_num > start_num:
                result.append(f"{start_num}->{end_num}")
            else:
                result.append(f"{start_num}")

        return result

    def summaryRanges2(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [f"{nums[0]}"]

        result = []
        temp_result = []

        for num in nums:
            if len(temp_result) == 0:
                temp_result.append([num, num])

            elif len(temp_result) > 0 and temp_result[-1][1] + 1 == num:
                temp_result[-1][1] = num

            else:
                temp_result.append([num, num])

        for left, right in temp_result:
            if right > left:
                result.append(f"{left}->{right}")
            else:
                result.append(f"{left}")

        return result


solution = Solution()

print(solution.summaryRanges1(nums=[0, 1, 2, 4, 5, 7]))
print(solution.summaryRanges1(nums=[0, 2, 3, 4, 6, 8, 9]))
