class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {')':'(', '}':'{', ']':'['}
        stack = []

        for x in s:
            if x not in pairs:
                # that means it is an opening brace
                stack.append(x)
            else:
                # that means it is potentially a closing brace
                if stack and stack[-1] == pairs[x]:
                    # need to check if stack is empty first
                    stack.pop()
                else:
                    return False
        return not stack
