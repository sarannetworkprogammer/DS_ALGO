A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]

from collections import deque
class TreeNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(A[0])

q = deque()
q.append(root)

i =1

while q:

    curr = q.popleft()
    if curr.val == -1:
        continue
    val_left = A[i]
    val_right = A[i+1]
    i = i+2
    if val_left == -1:
        curr.left = None
    else:
        curr.left = TreeNode(val_left)
        q.append(curr.left)
    
    if val_right == -1:
        curr.right = None
    else:
        curr.right = TreeNode(val_right)
        q.append(curr.right)

print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)

