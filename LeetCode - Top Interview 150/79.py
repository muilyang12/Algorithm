# 79. Word Search
# https://leetcode.com/problems/word-search/


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, index, is_visited):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if index >= len(word):
                return False

            if is_visited[i][j]:
                return False

            if board[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            is_visited[i][j] = True

            result = (
                dfs(i + 1, j, index + 1, is_visited)
                or dfs(i - 1, j, index + 1, is_visited)
                or dfs(i, j + 1, index + 1, is_visited)
                or dfs(i, j - 1, index + 1, is_visited)
            )

            is_visited[i][j] = False

            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue

                is_visited = [
                    [False for _ in range(len(board[0]))] for __ in range(len(board))
                ]

                result = dfs(i, j, 0, is_visited)

                if result:
                    return True

        return False
