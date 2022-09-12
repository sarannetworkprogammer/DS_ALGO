class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# now creating class for linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    

    # inserting after nth node


    def insertAfter(self,prev_node, new_data):

        if prev_node is None:
            print("Prev_node data is required")
            return
        
        new_node = Node(new_data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node

    
    # adding end of linked list so we have to go through entire linked list


    def append(self, new_data):

        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return
        
        # else  we have to traver

        last = self.head
        index = 1
        while (last.next):
            last = last.next  
        last.next = new_node

    
    # printing the linked_list

    def printList():
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

# now creating a list 


if __name__ == "__main__":


