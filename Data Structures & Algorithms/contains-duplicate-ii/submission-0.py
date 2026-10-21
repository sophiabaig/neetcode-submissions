class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        # int array nums
        # int k
        # return True IF
        # indices i and j in array where nums[i] == nums[j]
        # abs(i - j) <= k

        # difference between i and j less than or equal to k
        # return False if not

        left = 0
        seen = set()

        for right in range(len(nums)):

            if (right - left) > k:
                seen.remove(nums[left])
                left+=1
            
            if nums[right] in seen:
                return True

            seen.add(nums[right])


        return False