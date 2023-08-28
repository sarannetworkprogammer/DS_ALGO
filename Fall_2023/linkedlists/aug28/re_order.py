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


def print_linkedlist(head):
    curr = head
  
    while curr:
        print(curr.val,"->",end="")
        curr = curr.next



print(f"Printing the linkedlist")
print_linkedlist(head)



cur = head
arr1 = []

while cur:
    arr1.append(cur.val)
    cur = cur.next


print("\n")
print(arr1)

n = len(arr1)

print(f"length = {n}")

i = 0
j = n-1

list1 =[]

while(i<=j):

    if i==j:
        list1.append(arr1[i])

    else:
        list1.append(arr1[i])
        list1.append(arr1[j])
    i = i +1
    j = j-1


print(f"list1 = {list1}")









