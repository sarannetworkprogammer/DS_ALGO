class TreeNode:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]



def dfs(A):
    temp = A.pop(0)
    if temp == -1:
        return None
    
    node = TreeNode(temp)
    node.left = dfs(A)
    node.right= dfs(A)
    return node

ans = dfs(A)

print(ans.val)
print(ans.left.val)
print(ans.left.left.val)
#rint(ans.left.right.val)
print(ans.right.val)
