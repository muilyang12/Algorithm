# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alphabet_mapper = {}

        for i in range(len(s)):
            if not s[i] in alphabet_mapper:
                if t[i] in alphabet_mapper.values():
                    return False

                alphabet_mapper[s[i]] = t[i]

                continue

            if alphabet_mapper[s[i]] != t[i]:
                return False

        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        alphabet_mapper = {}

        for i in range(len(s)):
            if s[i] in alphabet_mapper.keys() and alphabet_mapper[s[i]] != t[i]:
                return False

            elif s[i] in alphabet_mapper.keys() and alphabet_mapper[s[i]] == t[i]:
                continue

            elif (
                not s[i] in alphabet_mapper.keys() and t[i] in alphabet_mapper.values()
            ):
                return False

            alphabet_mapper[s[i]] = t[i]

        return True


solution = Solution()

print(solution.isIsomorphic2(s="egg", t="add"))
print(solution.isIsomorphic2(s="foo", t="bar"))
print(solution.isIsomorphic2(s="abcd", t="abab"))
