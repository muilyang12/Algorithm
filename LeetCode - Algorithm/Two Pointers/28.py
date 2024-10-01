# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = 0

        while right < len(haystack) and right - left < len(needle):
            if haystack[left] != needle[0]:
                left += 1
                right += 1
            elif haystack[right] == needle[right - left]:
                right += 1
            else:
                left = left + 1
                right = left

        if right - left == len(needle):
            return left

        return -1
