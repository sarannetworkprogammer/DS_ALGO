class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    # function to addd new node

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The menitoned data is absent")
            return
        

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def list1print(self):
        printval = self.headval

        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list1 = SLinkedList()

list1.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("wed")

list1.headval.nextval = e2
e2.nextval = e3

list1.Inbetween(e2,"Fri")

list1.list1print()