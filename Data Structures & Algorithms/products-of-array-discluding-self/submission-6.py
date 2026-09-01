class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_arr = [0]*len(nums)

        for i, x in enumerate(nums):
            if i == 0:
                prefix_arr[i]=1
            else:
                prefix_arr[i]=prefix_arr[i-1]*nums[i-1]
        
        result = [0]*len(nums)
        
        for i, x in reversed(list(enumerate(nums))):
            if i == len(nums)-1:
                result[i]=1
            else:
                result[i]=result[i+1]*nums[i+1]
        
        for i, x in enumerate(nums):
            result[i]=prefix_arr[i]*result[i]

        return result
        