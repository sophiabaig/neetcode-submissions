class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for o in operations:

            if o == '+':
                a = stack[-1]
                b = stack[-2]

                c = a + b
                stack.append(c)
            
            elif o == 'D':
                a = stack[-1]
                c = a * 2
                stack.append(c)

            elif o == 'C':
                stack.pop()
            else:
                stack.append(int(o))

        result = 0

        for s in stack:
            result += s
        return result





        