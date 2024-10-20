from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        targets = []

        for num in numsSet:
            if num - 1 in numsSet:
                continue

            targets.append(num)

        count = 0

        for target in targets:
            currentCount = 0

            increase = 0

            while target + increase in numsSet:
                currentCount += 1
                increase += 1

            if currentCount > count:
                count = currentCount

        return count
