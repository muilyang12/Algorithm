# 139. Word Break
# https://leetcode.com/problems/word-break/

from typing import List


class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)

        memo = [False] * (len(s) + 1)
        memo[0] = True

        wordMaxLength = max(map(lambda x: len(x), wordDict))

        current = 1

        while current < len(memo):
            for j in range(current, max(current - wordMaxLength, 0) - 1, -1):
                target = s[j:current]

                if target in wordDictSet and memo[j]:
                    memo[current] = True

                    break

            current += 1

        return memo[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)

        memo = [False] * (len(s) + 1)
        memo[0] = True

        current = 0

        while current < len(memo):
            if not memo[current]:
                current += 1

                continue

            for word in wordDict:
                length = len(word)

                if current + length > len(s):
                    continue

                target = s[current : current + length]

                if target in wordDictSet:
                    memo[current + length] = True

            current += 1

        return memo[-1]
