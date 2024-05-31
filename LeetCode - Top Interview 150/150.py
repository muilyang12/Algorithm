# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/


from typing import List


class Solution:
    def evalRPN1(self, tokens: List[str]) -> int:
        copied_tokens = tokens[:]

        operators = ["+", "-", "*", "/"]

        first = 0
        second = 1
        third = 2

        while len(copied_tokens) > 1:
            if second >= len(copied_tokens) - 1:
                first = 0
                second = 1
                third = 2

            if (
                copied_tokens[first] in operators
                or copied_tokens[second] in operators
                or not copied_tokens[third] in operators
            ):
                first += 1
                second += 1
                third += 1

                continue

            if copied_tokens[third] == "+":
                copied_tokens[first] = str(
                    int(copied_tokens[first]) + int(copied_tokens[second])
                )
            elif copied_tokens[third] == "-":
                copied_tokens[first] = str(
                    int(copied_tokens[first]) - int(copied_tokens[second])
                )
            elif copied_tokens[third] == "*":
                copied_tokens[first] = str(
                    int(copied_tokens[first]) * int(copied_tokens[second])
                )
            else:
                copied_tokens[first] = str(
                    int(int(copied_tokens[first]) / int(copied_tokens[second]))
                )

            del copied_tokens[third]
            del copied_tokens[second]

        return int(copied_tokens[0])

    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(second + first)
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif token == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(second * first)
            elif token == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(token))

        return stack[0]


solution = Solution()

print(solution.evalRPN2(tokens=["2", "1", "+", "3", "*"]))
print(solution.evalRPN2(tokens=["4", "13", "5", "/", "+"]))
print(
    solution.evalRPN2(
        tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
