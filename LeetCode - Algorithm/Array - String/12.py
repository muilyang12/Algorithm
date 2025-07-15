# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        valueToSymbolMapper = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        values = list(valueToSymbolMapper.keys())

        currentNum = num
        index = 0

        while currentNum > 0:
            targetValue = values[index]

            if currentNum >= targetValue:
                currentNum -= targetValue
                result += valueToSymbolMapper[targetValue]
            else:
                index += 1

        return result
