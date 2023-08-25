class ListNode:
    
    def __init__(self,x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l2 = ListNode(2)
l3=  ListNode(3)
l4 = ListNode(4)

head = l1
l1.next = l2
l2.next = l3
l3.next = l4

def print_linkedlist(head):
    curr = head
    while curr:
        print(curr.val,"->",end="")
        curr = curr.next

print(f"Printing the linkedlist")
print_linkedlist(head)

def count_linkedlist(head):
    count = 0
    curr = head
    while curr:
        count = count +1
        curr = curr.next
    return count 

count = count_linkedlist(head)

print(f"\ncount_nodes ={count}")

def removenthfromend(head,B):

    count = count_linkedlist(head)
    target = count-B
    curr = head

    if target <= 0:
        tmp = head.next
        head = None
        head = tmp

    else:
        remove_count =0
        while curr:
            remove_count = remove_count +1
            if remove_count == target:
                curr.next = curr.next.next
            curr = curr.next
    
    print_linkedlist(head)


removenthfromend(head,5)



