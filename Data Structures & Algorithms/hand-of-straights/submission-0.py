import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        frequencies = {}

        for h in hand:
            if h not in frequencies:
                frequencies[h]=0
            frequencies[h]+=1
        
        heapq.heapify(hand)

        while len(frequencies) > 0:

            min_val = heapq.heappop(hand)
            if min_val not in frequencies:
                continue

            for i in range(min_val, min_val + groupSize):
                if i in frequencies:
                    frequencies[i]-=1
                    if frequencies[i]==0:
                        del frequencies[i]
                else:
                    return False

        return True

