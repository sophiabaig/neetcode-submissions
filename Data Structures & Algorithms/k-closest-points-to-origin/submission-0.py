import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        d_heap = []

        for i in range(len(points)):

            x, y = points[i]

            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(d_heap, (distance, i))


        output = []

        for i in range(k):

            distance, p_index = heapq.heappop(d_heap)

            output.append(points[p_index])

        return output






        