class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2
            cur = nums[mid]

            if cur == target:
                return mid
            elif cur > target:
                high = mid - 1
            else:
                low = mid + 1
    
        return -1
        