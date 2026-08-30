class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # create set to track what has been seen
        frequencies = set()

        # loop through nums and track occurences
        for x in nums:
            if x in frequencies:
                return True # seen this num before
            else:
                frequencies.add(x)
        
        return False
        


