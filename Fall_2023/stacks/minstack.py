class MinStack:


    def __init__(self):
        self.stack =[]
        self.minstack =[]

    def push(self,val):
        self.stack.append(val)
        if self.minstack:
            val = min(val, self.minstack[-1])

        self.minstack.append(val)

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]
   

    def getmin(self):
        return self.minstack[-1]