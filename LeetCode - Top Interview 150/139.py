# 139. Word Break
# https://leetcode.com/problems/word-break/


from typing import List


class Solution:
    # time complexity: O(nmk) (n: length of s, m: length of wordDict, k: average length of each word in wordDict)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)

        memo = [False] * (length + 1)
        memo[0] = True

        for i in range(1, length + 1):
            for word in wordDict:
                prev_index = i - len(word)

                if prev_index < 0:
                    continue

                if not memo[prev_index]:
                    continue

                if s[prev_index:i] == word:
                    memo[i] = memo[prev_index]

        return memo[-1]
