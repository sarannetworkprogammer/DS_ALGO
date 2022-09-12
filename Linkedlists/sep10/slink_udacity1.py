class Element:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head
        #print(self.head.value)
        

    def append(self,new_element):
        current = self.head
        print(current.value)
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            print(current.next.value)
        else:
            self.head = new_element

    
    def get_position(self, position):

        self.position = position
        current = self.head
        count = 1
        while (current):
            if (count == self.position):
                return current
            count = count + 1
            current = current.next
        return



    def insert(self, new_element, position):
        self.new_element = new_element
        self.position = position
        current = self.head
        index = 1
        while current:
            if (index == self.position-1):
                self.new_element.next = current.next
                current.next = new_element
            
            current = current.next
            index == index + 1

    

    # printing the linked list

    def list1print(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next
        










#creating some elements or nodes

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# start setting up a linked list

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print(f"position {ll.get_position(3).value}")

ll.insert(e4,3)
print(ll.get_position(3).value)

print("entire list")

ll.list1print()