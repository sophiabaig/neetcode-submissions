class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxLength = 0

        currLength = 0

        for x in nums:

            if x == 1:
                currLength+=1
                maxLength = max(currLength, maxLength)
            elif x == 0:
                currLength = 0
            
        
        return maxLength


        