class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {'[':']', '{':'}', '(':')'}
        stack = []

        for x in s:
            if x in parentheses:
                stack.append(x)
            else:
                if len(stack) > 0:
                    opening = stack.pop()
                    if not parentheses[opening]==x:
                        return False
                else:
                    return False
        
        return len(stack)==0