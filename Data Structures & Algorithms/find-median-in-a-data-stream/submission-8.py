import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
        
    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]: 
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, num * -1)
        
        if len(self.small) > (len(self.large) + 1):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)
        elif len(self.large) > (len(self.small) + 1):
            val = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return ((self.small[0] * -1)+ self.large[0]) / 2
        