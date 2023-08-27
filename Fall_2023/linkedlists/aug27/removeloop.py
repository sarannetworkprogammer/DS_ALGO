class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None



l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)
l9 = ListNode(9)


head = l1
l1.next =l2
l2.next =l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9
l9.next = l4

def print_linkedlist(head):
    curr = head
    count = 0
    while curr:
        print(curr.val,"->",end="")
        curr = curr.next
        count = count +1
        if count == 10:
            break

print(f"Printing the linkedlist")
print_linkedlist(head)

slow = head
fast = head

while True:

    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        print(f"\nLoop is detected")
        print(f"slow ={slow.val}")
        print(f"fast = {fast.val}")
        break


slow = head

print(f"after break slow.val = {slow.val}")


cnt =0
while True:

    cnt = cnt +1
    if cnt ==10:
       break

    if slow.next == fast.next:
       print(f"in_loop_slow ={slow.val}")
       print(f"in_loop_fast = {fast.val}")

       break
   
    
   
    slow = slow.next
    fast = fast.next

fast.next = None

print("After removing loop")

print_linkedlist(head)



  