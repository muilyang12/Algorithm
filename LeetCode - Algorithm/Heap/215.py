# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/


from typing import List
import heapq


class Solution:
    # time complexity: O(n log n + k log n) = O(n log n)
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > len(nums) - k + 1:
                heapq.heappop(minHeap)

        return heapq.heappop(minHeap)

    # time complexity: O(k + 2 (n - k) log k) = O(n log k)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for num in nums[k:]:
            heapq.heappush(minHeap, num)
            heapq.heappop(minHeap)

        return minHeap[0]


"""
For returning the final result, I don't need to use heapq.pop(minHeap); 
instead, I can simply use minHeap[0].
"""
