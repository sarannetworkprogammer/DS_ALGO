class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval =None

    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        print(f"self.headvalue ={self.headval}")
        last = self.headval
        print(f"last = {last.nextval}")
        while(last.nextval):
            last = last.nextval
            print(f"inwhile {last}")

        last.nextval = NewNode

    def list1print(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list1 = SLinkedList()

list1.headval = Node("mon")
e2 = Node("tue")
e3 = Node("wed")

list1.headval.nextval = e2
e2.nextval = e3
list1.AtEnd("Thu")
list1.list1print()