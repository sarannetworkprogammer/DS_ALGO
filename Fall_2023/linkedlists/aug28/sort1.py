class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None

l1 = ListNode(10)
l2 = ListNode(2)
l3 = ListNode(30)
l4 = ListNode(4)
l5 = ListNode(5)


head =l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

list1 = []

def print_linkedlist(head):
    curr = head
  
    while curr:
        list1.append(curr.val)
        print(curr.val,"->",end="")
        curr = curr.next


print(f"Printing the linkedlist")
print_linkedlist(head)

list1.sort()

print(list1)