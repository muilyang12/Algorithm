# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(letters, left_count, right_count):
            if left_count > n or right_count > n:
                return

            if left_count == n and right_count == n:
                result.append(letters)

                return

            if left_count == right_count:
                dfs(letters + "(", left_count + 1, right_count)
            elif left_count > right_count:
                dfs(letters + "(", left_count + 1, right_count)
                dfs(letters + ")", left_count, right_count + 1)

        dfs("", 0, 0)

        return result
