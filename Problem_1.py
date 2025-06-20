# // Time Complexity : O(1) - amortized
# // Space Complexity : O(1)
    
class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def moveToStack2(self):
        for i in range(len(self.stack)):
            self.stack2.append(self.stack.pop())

    def push(self, x: int) -> None:
        self.stack.append(x)
    
    def pop(self) -> int:
        if(len(self.stack2)==0):
            self.moveToStack2()
        return self.stack2.pop()

    def peek(self) -> int:
        if(len(self.stack2)==0):
            for i in range(len(self.stack)):
                self.stack2.append(self.stack.pop())
        return self.stack2[-1]

        return self.stack[-1]  

    def empty(self) -> bool:
        if(len(self.stack) == 0):
            if(len(self.stack2) == 0): 
                return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()