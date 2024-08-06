# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        num_to_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        result = []

        def dfs(current, digits_left):
            if not digits_left:
                result.append(current)

                return

            current_digit = digits_left[0]

            for char in num_to_chars[current_digit]:
                dfs(current + char, digits_left[1:])

        dfs("", list(digits))

        return result
