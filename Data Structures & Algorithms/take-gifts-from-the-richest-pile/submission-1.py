import math
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        max_gifts = [-x for x in gifts]
        heapq.heapify(max_gifts)

        for i in range(k):
            chosen = heapq.heappop(max_gifts) * -1
            heapq.heappush(max_gifts, math.isqrt(chosen) * -1)

        output = 0
        for i in range(len(max_gifts)):
            output+=heapq.heappop(max_gifts) * -1

        return output


