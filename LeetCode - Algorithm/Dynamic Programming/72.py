# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]

        for i in range(len(word1)):
            memo[i][len(word2)] = len(word1) - i

        for j in range(len(word2)):
            memo[len(word1)][j] = len(word2) - j

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    memo[i][j] = memo[i + 1][j + 1]

                    continue

                afterInsert = 1 + memo[i][j + 1]
                afterDelete = 1 + memo[i + 1][j]
                afterReplace = 1 + memo[i + 1][j + 1]

                memo[i][j] = min(afterInsert, afterDelete, afterReplace)

        return memo[0][0]


# word1 = "horse", word2 = "ros"
"""
   r o s
h [0,0,0,5]
o [0,0,0,4]
r [0,0,0,3]
s [0,0,0,2]
e [0,0,1,1]
  [3,2,1,0]
"""
