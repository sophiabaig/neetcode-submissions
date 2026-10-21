class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for o in operations:

            if o == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            
            elif o == 'D':
                a = stack[-1]
                stack.append(a * 2)

            elif o == 'C':
                stack.pop()
            else:
                stack.append(int(o))

        result = 0

        for s in stack:
            result += s
        return result





        