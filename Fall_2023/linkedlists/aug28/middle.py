class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)


head =l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

slow = head
fast = head


while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

print(f"middle ={slow.val}")