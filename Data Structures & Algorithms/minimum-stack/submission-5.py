class MinStack:

    # the trick is: i only need to track the minimums currently in the stack
    


    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum) == 0:
            self.minimum.append(val)
        elif val <= self.getMin():
            self.minimum.append(val)
        
       # print(self.stack, self.minimum)

    def pop(self) -> None:
        val = self.stack.pop()
        if len(self.minimum)>0 and val == self.getMin():
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
