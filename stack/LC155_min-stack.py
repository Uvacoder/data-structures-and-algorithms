class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myStack = []
        self.minimum = []   # this is used to find the minimum in the list
        

    def push(self, x: int) -> None:
        self.myStack.append(x)
        if not self.minimum:        # if minimum is empty:
            self.minimum.append(x)
        else:                       # if minimum is not empty:
            self.minimum.append( min(self.minimum[-1], x) )
        

    def pop(self) -> None:
        self.minimum.pop()
            
        return self.myStack.pop()

    def top(self) -> int:
        return self.myStack[-1]

    def getMin(self) -> int:
        return min(self.myStack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
