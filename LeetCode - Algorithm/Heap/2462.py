# 2462. Total Cost to Hire K Workers
# https://leetcode.com/problems/total-cost-to-hire-k-workers/

from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) <= 2 * candidates:
            minQueue = costs[:]
            heapq.heapify(minQueue)

            values = [heapq.heappop(minQueue) for _ in range(k)]

            return sum(values)

        leftMinQueue = []
        rightMinQueue = []

        values = []

        for i in range(candidates):
            heapq.heappush(leftMinQueue, costs[i])

            heapq.heappush(rightMinQueue, costs[-(i + 1)])

        leftCount = candidates
        rightCount = candidates

        while len(values) < k:
            if leftMinQueue and (
                not rightMinQueue or leftMinQueue[0] <= rightMinQueue[0]
            ):
                target = heapq.heappop(leftMinQueue)

                if leftCount + rightCount < len(costs):
                    leftCount += 1

                    heapq.heappush(leftMinQueue, costs[leftCount - 1])

            else:
                target = heapq.heappop(rightMinQueue)

                if leftCount + rightCount < len(costs):
                    rightCount += 1

                    heapq.heappush(rightMinQueue, costs[-rightCount])

            values.append(target)

        return sum(values)


"""
costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]. k = 11. candidates = 2
         ^     ^                               ^     ^
        [17, 25], 3, 3
"""
