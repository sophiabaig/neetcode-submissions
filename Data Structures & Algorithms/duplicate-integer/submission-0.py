class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}

        for x in nums:
            if x in duplicates:
                return True
            else: 
                duplicates[x]=1
                
        return False
        