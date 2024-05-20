# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/


from typing import List


class Solution:
    def count_alphabet1(self, string: str):
        result = {}

        for alphabet in string:
            if alphabet in result:
                result[alphabet] += 1
            else:
                result[alphabet] = 1

        return result

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        result = []
        counts = []

        for str in strs:
            count = self.count_alphabet1(str)

            if not count in counts:
                result.append([str])
                counts.append(count)

            else:
                target_index = counts.index(count)
                result[target_index].append(str)

        return result

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for str in strs:
            list_str = list(str)
            sorted_str = "".join(sorted(list_str))

            if sorted_str in result:
                result[sorted_str].append(str)
            else:
                result[sorted_str] = [str]

        return list(result.values())


solution = Solution()

print(solution.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams1([""]))
print(solution.groupAnagrams1(["a"]))

print(solution.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams2([""]))
print(solution.groupAnagrams2(["a"]))
print(solution.groupAnagrams2(["bdddddddddd", "bbbbbbbbbbc"]))
