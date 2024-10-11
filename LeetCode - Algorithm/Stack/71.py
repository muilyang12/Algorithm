# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path: str) -> str:
        resultPathes = []

        originalPathes = path.split("/")

        for pathElem in originalPathes:
            if pathElem == "":
                continue
            elif pathElem == ".":
                continue
            elif pathElem == "..":
                if resultPathes:
                    resultPathes.pop()
            else:
                resultPathes.append(pathElem)

        result = "/"

        for index, pathElem in enumerate(resultPathes):
            result += pathElem

            if index < len(resultPathes) - 1:
                result += "/"

        return result


"""
The hardest part of this problem is recognizing that it's a 'Stack' problem.
"""
