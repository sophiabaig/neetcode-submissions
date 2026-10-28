import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        output = nums.copy()
        min_heap = []

        for i, o in enumerate(output):
            heapq.heappush(min_heap, (o, i))
        
        for i in range(k):
            num, i = heapq.heappop(min_heap)
            output[i] *= multiplier
            heapq.heappush(min_heap, (output[i], i))

        return output

        

