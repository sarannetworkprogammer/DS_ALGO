class TreeNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]


def dfs():
    if A[i] == -1:
        i = i+1
        return None
    node = TreeNode(i)
    i = i+1
    node.left = dfs()
    node.right = dfs()
    return node

i = 0
ans =dfs()

print(f"ans= {ans}")
