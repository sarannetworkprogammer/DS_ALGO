#Node class

class Node:
    def __init__(self,data):  # function to initialize node object
        self.data = data   
        self.next = None  # none nothing but null


#Linkedlist class

class LinkedList:

    def __init__(self):
        self.head = None

# inserting node at given position either its front or tail or at nth position
    # function inserting at first position these specially called as statck 
    def push(self, new_data):
        # first create a node for new data and keep the data

        new_node = Node(new_data)

        #3. Make next of new node as a head

        new_node.next = self.head

        #4. move the head point to new node

        self.head = new_node
    

    # function inserting a new node after the given previous_node 


    def insertAfter(self, prev_node, new_data):

        # checking previous node exists or not

        if prev_node is None:
            print("The given previous node must be in linkedlist")
            return



        new_node = Node(new_data)
        # make next of new node as next of previous node
        new_node.next = prev_node.next
        # 5. make 
        prev_node.next = new_node


    # function for adding a node at the end which is nothing but appending to existing 

    def append(self, new_data):
        #1.create a new node
        #2. put data
        #2. as it is last element next will be null

        new_node = Node(new_data)
        
        new_node.next = None

        # if linked list is empty make the new node as head 
        if self.head is None:
            self.head = new_node
            return
        
        # else we have to traverse the last node

        last = self.head
        while (last.next):
            last = last.next

        #6. change next of last node
        last.next = new_node


    # deleting a node 


    def deleteNode(self,key):

        #head node

        temp = self.head

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        
    
    # seach for the key to be deleted 

        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if (temp == None):
            return
        
        #if key was not present in linked list 

        prev.next = temp.next
        temp = None


    # Deleting a node at Given Position

    def deleteNodeAtGivenPosition(self,position):
        if self.head is None:
            return
        
        index = 0

        current = self.head

        while current.next and index < position:
            previous = current
            current = current.next
            index += 1

        if index == 0:
            self.head == self.head.next
        
        else:
            previous.next = current.next
            current = None

    
    # searching nth node

    def getNth(self,index):

        current = self.head # intilaise temp
        count = 0

        while (current):
            if count == index:
                return current.data
            
            count = count + 1
            current = current.next
            
        
        assert(False) # for non existennt index posiition

        return 0


    def insertNodeAtGivenPosition(self,position,new_data):
        

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        index = 0

        current = self.head

        while (current.next):
            if (index == position-1):
                break
            previous = current
            current = current.next
            index += 1
        
        
        new_node.next = current.next
        current.next = new_node

         















    #printing the linked list

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data , end=" ->")
            temp = temp.next


# now  creating list

if __name__ == "__main__":

    # creating object of empty list
    llist = LinkedList()

    # insert 6

    llist.append(6)

    # insert at the front 7->6

    llist.push(7)

    #insert 1 at fronnt 1->7->6
    
    llist.push(1)

    #insert 4 at the end  1->7->6->4

    llist.append(4)

    # insert 8 after 7 so linked list becomes 

    llist.insertAfter(llist.head.next, 8)

    print("created linked list")

    llist.printList()

    llist.deleteNode(1)
    print("\n")
    llist.printList()
    
    print("Element at index 3 ", llist.getNth(3))

    llist.insertNodeAtGivenPosition(1,25)

    print("\n")

    llist.printList()