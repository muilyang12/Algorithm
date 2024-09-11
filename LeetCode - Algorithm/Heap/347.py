# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/


from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountMapper = defaultdict(int)

        for num in nums:
            numCountMapper[num] += 1

        minHeap = []

        for num, count in numCountMapper.items():
            heapq.heappush(minHeap, (-count, num))

        result = []

        for _ in range(k):
            count, num = heapq.heappop(minHeap)
            result.append(num)

        return result
