class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # create hashmap to track frequencies
        # key = num, value = frequency
        frequencies = {}

        # loop through nums and track occurences
        for x in nums:
            if x in frequencies:
                frequencies[x]+=1
            else:
                frequencies[x]=1

        # loop through frequencies and exit if > 1
        # return true on early exit, else return false
        for num, frequency in frequencies.items():
            if frequency > 1:
                return True
        
        return False
        