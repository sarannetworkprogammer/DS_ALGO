from collections import deque
class TreeNode:

    def __init__(self,val):

        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

q = deque()
q.append(root)

ans =[]

print(f"q_len ={len(q)}")

count_level = 0

while q:
    q_len = len(q)
    level =[]

    for i in range(q_len):
        temp = q.popleft()
        level.append(temp.val)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    
    if count_level%2 == 0:
        ans.append(level)
    else:
        ans.append(level[::-1])
    count_level = count_level+1

print(f"result ={ans}")
    

