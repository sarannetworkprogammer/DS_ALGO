class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:


    def __init__(self):
        self.head = Node("head")
        self.size =0

    #string representation of stack

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out = out + str(cur.value) +"->"
            cur = cur.next
        return out
    

    # get current size of the stack

    def getSize(self):
        return self.size

    # check if stack is empty

    def isEmpty(self):
        return self.size == 0

    #Get top item of the stack

    def peek(self):

        #sanitary check to see if we

        if self.isEmpty():
            raise Exception("peeking from empty stack")
        return self.head.next.value
    

    # push a value to stack

    def push(self,value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    # remove a value from stack and return

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    
if __name__ == "__main__":
    stack = Stack()
    for i in range(1,15):
        stack.push(i)
    print(f"stack = {stack}")

