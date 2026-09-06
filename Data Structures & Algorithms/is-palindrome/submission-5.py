class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        lower_s = s.lower()

        while left < right:
            while not lower_s[left].isalnum() and left < right:
                left+=1
            while not lower_s[right].isalnum() and left < right:
                right-=1
            
            if not lower_s[left]==lower_s[right]:
                return False
            
            left+=1
            right-=1
        
        return True


        