# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    # Sliding Window
    # time complexity: O(n ^ 2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left = 0
        right = 0

        result = 0

        while right < len(s):
            target = s[left : right + 1]
            targetSet = set(target)

            if len(target) == len(targetSet):
                result = max(result, len(target))
                right += 1
            else:
                left += 1

        return result
