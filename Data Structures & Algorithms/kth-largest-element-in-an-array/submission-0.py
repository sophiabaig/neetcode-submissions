import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k_heap = []

        for n in nums:

            heapq.heappush(k_heap, n)

            if len(k_heap) > k:
                heapq.heappop(k_heap)

        return heapq.heappop(k_heap)
        