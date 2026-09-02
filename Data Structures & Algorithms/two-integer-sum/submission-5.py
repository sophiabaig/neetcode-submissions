class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} # keep track of nums seen
        for index, num in enumerate(nums):

            complement = target - num # num needed for two sum
            if complement in seen: 
                # stop searching
                return [seen[complement], index]

            seen[num]=index

        