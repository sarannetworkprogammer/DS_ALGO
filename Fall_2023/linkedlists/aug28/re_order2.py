class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)


head =l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5



def print_linkedlist(head):
    curr = head
  
    while curr:
        print(curr.val,"->",end="")
        curr = curr.next



print(f"Printing the linkedlist")
print_linkedlist(head)


# finding the middle

slow = head
fast = head.next

while fast and fast.next:
    print(f"\nfast = {fast.val}")
    print(f"fast.next ={fast.next.val}")
    slow = slow.next
    fast = fast.next.next

# reverse the second half

curr = slow.next
prev = slow.next = None


print(f"second = {curr.val}")

while curr:
    tmp = curr.next
    curr.next = prev
    prev = curr
    curr = tmp

# merge two halfs

first = head
second = prev

print(f"{second.val}")


while second:
    tmp1 = first.next
    tmp2 = second.next
    print(f"tmp1 = {tmp1.val}")
    #print(f"tmp2 ={tmp2.val}")

    first.next = second
    second.next= tmp1

    first = tmp1
    second = tmp2




print(f"Printing the linkedlist")
print_linkedlist(head)