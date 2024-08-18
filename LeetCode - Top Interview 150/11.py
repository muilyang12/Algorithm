# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/


from typing import List


class Solution:
    def calculate_volume(self, height, left, right):
        if not left < right:
            return 0

        current_volume = (right - left) * min(height[left], height[right])

        return current_volume

    def maxArea1(self, height: List[int]) -> int:
        result = 0

        left = 0
        right = len(height) - 1

        while left < right:
            current_volume = self.calculate_volume(height, left, right)

            result = max(result, current_volume)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

    # Idea was nice. But the answer is wrong. :(
    def maxArea2(self, height: List[int]) -> int:
        result = 0

        left = 0
        right = len(height) - 1

        while left < right:
            current_volume1 = self.calculate_volume(height, left, right)
            current_volume2 = self.calculate_volume(height, left + 1, right)
            current_volume3 = self.calculate_volume(height, left, right - 1)

            result = max(result, current_volume1, current_volume2, current_volume3)

            left += 1
            right -= 1

        return result


solution = Solution()

print(solution.maxArea1(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(solution.maxArea1(height=[1, 1]))
print(solution.maxArea1(height=[2, 3, 10, 5, 7, 8, 9]))
