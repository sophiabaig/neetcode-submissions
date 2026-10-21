class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for o in operations:

            if o == '+':
                a = stack.pop()
                b = stack.pop()

                stack.append(b)
                stack.append(a)

                c = int(a) + int(b)
                stack.append(c)
            
            elif o == 'D':
                a = stack.pop()
                stack.append(a)
                c = int(a) * 2
                stack.append(c)

            elif o == 'C':
                stack.pop()
            else:
                stack.append(o)

        result = 0

        for s in stack:
            result += int(s)
        return result





        