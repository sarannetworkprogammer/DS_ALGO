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


cur = root

q = deque()
q.append(root)

print(f"intial ={q}")

ans = []


while q:
    print(f"each iteration= {q}")
    temp = q.popleft()
    if temp is not None:
        ans.append(temp.val)
        q.append(temp.left)
        q.append(temp.right)
    else:
        ans.append(-1)



print(f"ans ={ans}")