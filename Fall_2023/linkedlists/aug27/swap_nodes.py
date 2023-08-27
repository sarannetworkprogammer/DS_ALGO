class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

head = l1

def print_linkedlist(head):
    curr = head
  
    while curr:
        print(curr.val,"->",end="")
        curr = curr.next



print(f"Printing the linkedlist")
print_linkedlist(head)

def  swap_nodes(head):

    dummy = ListNode(0)
    dummy.next = head

    print(f"\ndummy={dummy.val}")

    prev = dummy
    cur = head

    while cur and cur.next:

        nextpair = cur.next.next

        second = cur.next

    # reverse the pair

        second.next = cur
        cur.next = nextpair
        prev.next = second

    #update the pointer

        prev = cur
        cur = nextpair




swap_nodes(head)

print(f"Printing after swaping")

