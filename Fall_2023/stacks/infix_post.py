class solution:

    def __init__(self,capacity):
        
        self.capacity = capacity
        self.top = -1
        
        self.stack =[]
        self.output =[]
        self.precedence = {"+": 1, "-":1, "*":2, "/":2, "^":3}


    def isoperand(self,ch):
        return ch.isalpha()
    
    def push(self,ch):
        self.top +=1
        self.stack.append(ch)

    def solve(self,A):

        res = ""

        for each in A:
            if self.isoperand(each):
                res.append(each)

            elif each =="(":
                self.push(each)

            elif each == ")":

                
