# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/


class Solution:
    # time complexity: O(3n) = O(n)
    # Splitting a string takes O(n) ('split' method)
    # Joining the elements of a list takes O(n)
    def simplifyPath1(self, path: str) -> str:
        result = []

        splited_path = path.split("/")

        for i in range(len(splited_path)):
            part = splited_path[i]
            if part == "..":
                if len(result) > 1:
                    result.pop()
                else:
                    continue

            elif part == ".":
                continue

            elif part == "" and i != 0:
                continue

            else:
                result.append(part)

        return "/".join(result) if len(result) > 1 else "/"

    # time complexity: O(3n) = O(n)
    def simplifyPath2(self, path: str) -> str:
        result = []

        splited_path = path.split("/")

        for part in splited_path:
            if part == "..":
                if result:
                    result.pop()
                else:
                    continue

            elif part == "." or part == "":
                continue

            else:
                result.append(part)

        return "/" + "/".join(result)


solution = Solution()

print(solution.simplifyPath2(path="/home/"))
print(solution.simplifyPath2(path="/home//foo/"))
print(solution.simplifyPath2(path="/home/user/Documents/../Pictures"))
print(solution.simplifyPath2(path="/../"))
print(solution.simplifyPath2(path="/.../a/../b/c/../d/./"))
print(solution.simplifyPath2(path="/a/../../b/../c//.//"))
print(solution.simplifyPath2(path="/../"))
