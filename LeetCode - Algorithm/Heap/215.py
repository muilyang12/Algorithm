# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/


from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > len(nums) - k + 1:
                heapq.heappop(minHeap)

        return heapq.heappop(minHeap)
