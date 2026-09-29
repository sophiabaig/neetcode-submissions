import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        s_heap = []

        for s in stones:
            heapq.heappush(s_heap, (s * -1))
        
        while len(s_heap) > 1:

            stone_x = heapq.heappop(s_heap) * -1
            stone_y = heapq.heappop(s_heap) * -1

            if stone_x == stone_y:
                continue
            elif stone_x > stone_y:
                stone_x = stone_x - stone_y
                heapq.heappush(s_heap, (stone_x * -1))
        
        if len(s_heap) == 1:
            return s_heap[0] * -1
        else: 
            return 0

        