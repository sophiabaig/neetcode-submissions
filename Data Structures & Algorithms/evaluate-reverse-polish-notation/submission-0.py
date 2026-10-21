class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = {"+", "-", "*", "/"}
        
        for t in tokens:

            if t in operators:
                a = stack.pop()
                b = stack.pop()
                
                if t == "+":
                    res = b + a
                elif t == "-":
                    res = b - a
                elif t == "*":
                    res = b * a
                elif t == "/":
                    res = int(b / a)
                stack.append(res)
            
            else:
                stack.append(int(t))

        return stack.pop()

