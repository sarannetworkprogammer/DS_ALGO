class UserQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 =[]
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return -1

        if len(self.stack2) == 0 and len(self.stack1) > 0:

            while len(self.stack1):
                temp = self.stack1.pop()
                self.stack2.append(temp)

        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return -1
        
        if len(self.stack2)==0 and len(self.stack1) > 0:

            while len(self.stack1):
                temp = self.stack1.pop()
                self.stack2.append(temp)
        
        return self.stack2[-1]


        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True

        return False





# Your UserQueue object will be instantiated and called as such:
# obj = UserQueue()
# obj.push(x)
# param2 = obj.pop()
# param3 = obj.peek()
# param4 = obj.empty()