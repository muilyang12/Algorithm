# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/


from collections import defaultdict
from typing import Dict


class Solution:
    # Time Limit Exceeded :(
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0

        targetAlphabetCounts = defaultdict(int)
        for char in t:
            targetAlphabetCounts[char] += 1

        isRightMoving = True

        result = ""

        while left <= right < len(s):
            if (
                not self.isAllAlphabetsIncluded(
                    s[left : right + 1], targetAlphabetCounts
                )
                and isRightMoving
            ):
                right += 1

            elif (
                self.isAllAlphabetsIncluded(s[left : right + 1], targetAlphabetCounts)
                and isRightMoving
            ):
                if not result or (result and right - left + 1 < len(result)):
                    result = s[left : right + 1]

                isRightMoving = not isRightMoving

                left += 1

            elif not isRightMoving and not s[left] in t:
                left += 1

            elif not isRightMoving and s[left] in t:
                isRightMoving = not isRightMoving

        return result

    def isAllAlphabetsIncluded(self, string: str, targetAlphabetCounts: Dict[str, int]):
        copiedCounts = targetAlphabetCounts.copy()

        for char in string:
            if char in copiedCounts:
                copiedCounts[char] -= 1

        for count in copiedCounts.values():
            if count > 0:
                return False

        return True

    def minWindow2(self, s: str, t: str) -> str:
        left = 0
        right = 0

        targetAlphabetCounts = defaultdict(int)
        for char in t:
            targetAlphabetCounts[char] += 1

        isRightMoving = True

        currentAlphabetCounts = defaultdict(int)
        currentAlphabetCounts[s[left]] += 1

        result = ""

        while left <= right < len(s):
            if (
                not self.doesCurrentIncludeAllAlphabets(
                    currentAlphabetCounts, targetAlphabetCounts
                )
                and isRightMoving
            ):
                right += 1
                if right < len(s):
                    currentAlphabetCounts[s[right]] += 1

            elif (
                self.doesCurrentIncludeAllAlphabets(
                    currentAlphabetCounts, targetAlphabetCounts
                )
                and isRightMoving
            ):
                if not result or (result and right - left + 1 < len(result)):
                    result = s[left : right + 1]

                isRightMoving = not isRightMoving

                currentAlphabetCounts[s[left]] -= 1
                left += 1

            elif not isRightMoving and not s[left] in t:
                currentAlphabetCounts[s[left]] -= 1
                left += 1

            elif not isRightMoving and s[left] in t:
                isRightMoving = not isRightMoving

        return result

    def doesCurrentIncludeAllAlphabets(
        self,
        currentAlphabetCounts: Dict[str, int],
        targetAlphabetCounts: Dict[str, int],
    ):
        for alphabet, count in targetAlphabetCounts.items():
            if currentAlphabetCounts[alphabet] < count:
                return False

        return True


"""
The reason why my code exceeded the time limit is due to the inefficiency in the isAllAlphabetsIncluded
function. The function checks the entire substring every time, even though only one letter was added or 
removed from the window. I should improve the code by avoiding the repeated full scan of the substring.
"""
