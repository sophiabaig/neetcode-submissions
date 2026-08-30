class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # normalize the word first
        word = ""
        for x in s:
            if x.isalnum():
                word+=x.lower()

        left = 0
        right = len(word)-1

        while left < right:
            if word[left]==word[right]:
                left+=1
                right-=1
            else:
                return False
        return True