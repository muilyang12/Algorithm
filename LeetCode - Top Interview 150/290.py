# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapper = dict()
        s_array = s.split(" ")

        if len(pattern) != len(s_array):
            return False

        for i in range(len(pattern)):
            if pattern[i] in mapper and mapper[pattern[i]] != s_array[i]:
                return False

            elif pattern[i] in mapper and mapper[pattern[i]] == s_array[i]:
                continue

            elif not pattern[i] in mapper and s_array[i] in mapper.values():
                return False

            mapper[pattern[i]] = s_array[i]

        return True


solution = Solution()

print(solution.wordPattern(pattern="abba", s="dog cat cat dog"))
print(solution.wordPattern(pattern="abba", s="dog cat cat fish"))
print(solution.wordPattern(pattern="aaaa", s="dog cat cat dog"))
