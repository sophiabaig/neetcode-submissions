class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min = val
        if self.minStack:
            cur_min = min(cur_min, self.minStack[-1])
        self.minStack.append(cur_min)
        cur_max = val
        if self.maxStack:
            cur_max = max(cur_max, self.maxStack[-1])
        self.maxStack.append(cur_max)
        
    def pop(self) -> None:
        if self.stack: 
            self.stack.pop()
            self.minStack.pop()
            self.maxStack.pop()
        
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        
    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None

    def getMax(self) -> int:
        return self.maxStack[-1] if self.maxStack else None
        
