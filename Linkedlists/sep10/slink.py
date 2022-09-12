""""

Node has two parameters one is : data parameter

next value : which is address of next parameter

Declaring a node with data , value initial values are none two parameters one is data val, one is reference other as nextval


"""
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# intial head value is none for single linked list class
class SLinkedList:
    def __init__(self):
        self.headval = None

    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)

            printval = printval.nextval


    def AtBegining(self, newdata):

        NewNode = Node(newdata)


    #now NewNode is object of node it has datavalue, next val, 

        NewNode.nextval = self.headval
        self.headval = NewNode



    


list1 = SLinkedList()  # creation of object

print(list1.headval)
print(type(list1.headval))
# elements in class can be accessed like this print(list1.headval)

list1.headval = Node("Mon") # creation of object for Node 
#print("\nafter assigning value\n")
#print(list1.headval)
#print(type(list1.headval))


e2 = Node("Tue")

print(f"e2 node datavalue = {e2.dataval}")

e3 = Node("wed")



print(f"e3 node data value = {e3.dataval}")

# linking first node to second node

list1.headval.nextval = e2

e2.nextval = e3 # linking secondnode to third node


list1.AtBegining("sun")



list1.listprint()


# inserting in the beginning 

