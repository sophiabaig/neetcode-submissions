class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        
        for i, x in enumerate(nums):
            if i == 0:
                prefix[i]=1 # nothing before index 0
            else:
                # should equal prev prefix times prev num
                prefix[i]=prefix[i-1]*nums[i-1]
            

        suffix = [0]*len(nums)

        for i, x in reversed(list(enumerate(nums))):
            if i==len(nums)-1:
                suffix[i]=1
            else:
                suffix[i]=suffix[i+1]*nums[i+1]

        product = []

        for i, x in enumerate(nums):
            product.append(prefix[i] * suffix[i])

        return product

