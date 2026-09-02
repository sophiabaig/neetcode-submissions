import heapq
# heapq.heappush(data, 0)
# popped_item = heapq.heappop(data)  # Returns 0
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for x in nums:

            if x in frequencies:
                frequencies[x]+=1
            else:
                frequencies[x]=1

        min_heap = []

        for num, freq in frequencies.items():
            heapq.heappush(min_heap, (freq, num))
        
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []

        for freq, num in min_heap:
            result.append(num)

        return result
            