class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev, cur = 1, 1

        for i in range(2, n + 1):
            temp = cur
            cur = cur + prev
            prev = temp
        
        return cur