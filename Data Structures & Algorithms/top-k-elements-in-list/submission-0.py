import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}

        for x in nums:
            if x in frequencies:
                frequencies[x]+=1
            else:
                frequencies[x]=1


        heap = []
        for element, freq in frequencies.items():
            heapq.heappush(heap, (freq, element))
            if len(heap) > k:
                heapq.heappop(heap)

        topK = []
        for x in heap:
            topK.append(x[1])

        return topK

