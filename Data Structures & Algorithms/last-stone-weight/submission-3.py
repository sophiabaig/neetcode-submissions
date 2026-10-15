import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        s_heap = []

        for stone in stones:
            heapq.heappush(s_heap, stone * -1)
        
        while len(s_heap) > 1:

            stone_x = heapq.heappop(s_heap) * -1
            stone_y = heapq.heappop(s_heap) * -1

            if stone_x != stone_y:
                stone_n = (stone_x - stone_y) * -1
                heapq.heappush(s_heap, stone_n)
        
        if len(s_heap) == 0:
            return 0
        else:
            return heapq.heappop(s_heap) * -1



        