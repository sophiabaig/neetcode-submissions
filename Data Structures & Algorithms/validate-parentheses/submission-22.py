class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {'[':']', '{':'}', '(':')'}
        stack = []

        for x in s:
            if x in parentheses:
                stack.append(x)
            elif not stack or parentheses[stack.pop()] != x:
                return False
        
        return len(stack)==0