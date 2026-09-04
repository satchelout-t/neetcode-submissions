class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if (len(self.stack)==0):
            current_min=val
        else:
            previous_min=self.stack[-1][1]
            if previous_min>val:
                current_min=val
            else:
                current_min=previous_min
        self.stack.append((val,current_min))
    def pop(self):
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]
        
