class MyQueue:

    def __init__(self):
        self.l1=[]
        self.l2=[]
        

    def push(self, x: int) -> None:
        while(len(self.l1)):
            i=self.l1.pop()
            self.l2.append(i)
        self.l1.append(x)
        while(self.l2):
            i=self.l2.pop()
            self.l1.append(i)
            

    def pop(self) -> int:
        return self.l1.pop()
        

    def peek(self) -> int:
        return self.l1[-1]
        

    def empty(self) -> bool:
        if(len(self.l1)):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()