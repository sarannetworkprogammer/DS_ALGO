class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
    
    def Atbegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
    

    # Function to remove node



