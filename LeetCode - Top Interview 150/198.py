# 198. House Robber
# https://leetcode.com/problems/house-robber/


from typing import List


class Solution:
    # 무언가 누적이라는 느낌이 들면 DP를 사용해야할 것 같네.
    # time complexity: O(n)
    def rob1(self, nums: List[int]) -> int:
        earning = []

        for i in range(len(nums)):
            money_stashed = nums[i]

            if i == 0:
                earning.append(money_stashed)

                continue

            if i == 1:
                earning.append(max(earning[i - 1], money_stashed))

                continue

            earning.append(max(earning[i - 2] + money_stashed, earning[i - 1]))

        return earning[-1]

    # time complexity: O(n)
    def rob2(self, nums: List[int]) -> int:
        earning = [nums[0]]
        if len(nums) >= 2:
            earning.append(max(earning[0], nums[1]))

        for i in range(2, len(nums)):
            money_stashed = nums[i]

            earning.append(max(earning[i - 2] + money_stashed, earning[i - 1]))

        return earning[-1]


solution = Solution()

print(solution.rob(nums=[1, 2, 3, 1]))
print(solution.rob(nums=[2, 7, 9, 3, 1]))
print(solution.rob(nums=[2, 7, 9, 3, 1]))
print(solution.rob(nums=[2, 1]))
