class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min = val
        if self.minStack:
            cur_min = min(cur_min, self.minStack[-1])
        self.minStack.append(cur_min)
        
    def pop(self) -> None:
        if self.stack: 
            self.stack.pop()
            self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
