# 373. Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/


from typing import List
from collections import defaultdict
import heapq


class Solution:
    # Time Limit Exceeded
    # time complexity: O(n * m * log (n * m))
    def kSmallestPairs1(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        hash = defaultdict(list)
        min_heap = []

        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2

                if not sum in min_heap:
                    heapq.heappush(min_heap, sum)

                hash[sum].append([num1, num2])

        result = []

        while len(result) < k:
            target_sum = heapq.heappop(min_heap)

            result.extend(hash[target_sum])

        return result[:k]

    # Time Limit Exceeded
    # time complexity: O(n * m * log (n * m))
    # When an array or tuple is inserted into a heap, the heap compares
    # the elements in the array or tuple starting from the first element.
    def kSmallestPairs2(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        min_heap = []

        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2

                heapq.heappush(min_heap, (sum, (num1, num2)))

        result = []

        for i in range(k):
            _, pair = heapq.heappop(min_heap)

            result.append(pair)

        return result

    def kSmallestPairs3(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        result = []
        min_heap = []
        visited = set()

        heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))

        while len(result) < k:
            _, i, j = heapq.heappop(min_heap)

            result.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return result
