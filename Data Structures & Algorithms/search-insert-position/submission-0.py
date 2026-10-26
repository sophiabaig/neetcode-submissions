class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        res = len(nums)
        low, high = 0, len(nums)-1

        while low <= high:

            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
                
        return res
        
