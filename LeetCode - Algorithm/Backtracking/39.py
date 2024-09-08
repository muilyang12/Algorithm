# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        self.makeCombinationList(
            candidates=candidates,
            target=target,
            current=[],
            currentSum=0,
            startIndex=0,
            result=result,
        )

        return result

    def makeCombinationList(
        self,
        candidates: List[int],
        target: int,
        current: List[int],
        currentSum: int,
        startIndex: int,
        result: List[List[int]],
    ):
        if currentSum > target:
            return

        if currentSum == target:
            result.append(current[:])
            return

        for i in range(startIndex, len(candidates)):
            number = candidates[i]
            current.append(number)

            self.makeCombinationList(
                candidates=candidates,
                target=target,
                current=current,
                currentSum=currentSum + number,
                startIndex=i,
                result=result,
            )

            current.pop()
