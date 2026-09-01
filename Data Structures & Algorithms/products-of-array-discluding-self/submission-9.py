class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [0]*len(nums)

        for i, x in enumerate(nums):
            if i == 0:
                result[i]=1
            else:
                result[i]=result[i-1]*nums[i-1]
        
        suffix_var = 1

        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums)-1:
                suffix_var=suffix_var*nums[i+1]
                result[i]=result[i]*suffix_var

        return result
        