# 134. Gas Station
# https://leetcode.com/problems/gas-station/

from typing import List


class Solution:
    # Time Limit Exceeded
    # time complexity: O(n^2)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)

        for index in range(length):
            if gas[index] < cost[index]:
                continue

            currentIndex = index
            gasTank = 0

            for i in range(length):
                gasTank += (
                    gas[self.adjustIndex(currentIndex + i, length)]
                    - cost[self.adjustIndex(currentIndex + i, length)]
                )

                if gasTank < 0:
                    break

            if gasTank >= 0:
                return index

        return -1

    def adjustIndex(self, index, length):
        if index < length:
            return index
        else:
            return index - length

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)

        diff = []
        totalCumulative = 0
        for i in range(length):
            diff.append(gas[i] - cost[i])
            totalCumulative += gas[i] - cost[i]

        if totalCumulative < 0:
            return -1

        startPoint = -1
        cumulative = -1
        for i in range(length):
            if cumulative < 0 and diff[i] < 0:
                continue

            if cumulative < 0 and diff[i] >= 0:
                startPoint = i
                cumulative = 0

            cumulative += diff[i]

            if cumulative < 0:
                startPoint = -1
                cumulative = -1

        return startPoint


# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]

# diff = [-2, -2, -2, 3, 3]
# diff = [3, -2, -2, 3, -2]
# diff = [2, -1, -1]
