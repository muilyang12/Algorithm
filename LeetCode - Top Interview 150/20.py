# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid1(self, s: str) -> bool:
        parentheses_pair = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for parenthesis in s:
            if parenthesis in parentheses_pair:
                stack.append(parentheses_pair[parenthesis])

                continue

            last_one = None
            if len(stack) > 0:
                last_one = stack.pop()

            if last_one != parenthesis:
                return False

        if len(stack) != 0:
            return False

        return True

    def isValid2(self, s: str) -> bool:
        parentheses_pair = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for parenthesis in s:
            if parenthesis in parentheses_pair:
                stack.append(parentheses_pair[parenthesis])

                continue

            if len(stack) == 0 or stack.pop() != parenthesis:
                return False

        if len(stack) != 0:
            return False

        return True


solution = Solution()

print(solution.isValid1(s="()"))
print(solution.isValid1(s="()[]{}"))
print(solution.isValid1(s="(]"))
print(solution.isValid1(s="["))
print(solution.isValid1(s="]"))
