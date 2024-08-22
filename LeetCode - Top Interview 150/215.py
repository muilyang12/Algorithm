# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/


from typing import List
import heapq
import math


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        copied_nums = list(map(lambda x: -x, nums))
        heapq.heapify(copied_nums)

        result = math.inf
        for i in range(k):
            result = heapq.heappop(copied_nums)

        return result

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
