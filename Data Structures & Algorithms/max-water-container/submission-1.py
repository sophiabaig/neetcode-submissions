class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            curr_area = width * height

            if curr_area > maxArea:
                maxArea = curr_area

            if heights[left]==height:
                left+=1
            else:
                right-=1
        
        return maxArea


        