class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums) # get rid of duplicates
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:
                # this is a start

                curr_length = 1
                while (num + 1 in num_set):
                    num += 1
                    curr_length += 1
                
                if curr_length > longest:
                    longest = curr_length

        return longest
            