# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        stringRows = ["" for _ in range(numRows)]

        for i in range(numRows):
            j = 0
            target = i + (numRows - 1) * 2 * j

            while target < len(s):
                stringRows[i] += s[target]

                j += 1

                if i == 0 or i == numRows - 1:
                    target = i + (numRows - 1) * 2 * j
                elif j % 2 == 0:
                    target = i + (numRows - 1) * j
                else:
                    target = i + (numRows - 1) * (j + 1) - 2 * i

        result = ""
        for row in stringRows:
            result += row

        return result
