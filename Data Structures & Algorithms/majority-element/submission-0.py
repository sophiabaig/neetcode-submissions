class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq_map = {}

        for n in nums:

            if n not in freq_map:

                freq_map[n]=0
            
            freq_map[n]+=1

            if freq_map[n] > (len(nums) / 2):

                return n
        
