class TreeNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(8)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(6)

root.right = TreeNode(13)
root.right.left = TreeNode(10)
root.right.right = TreeNode(15)
root.right.right.right = TreeNode(17)


# printing inorder traversal


def inorder(root):

    if root is None:
        return

    inorder(root.left)
    ans.append(root.val)
    inorder(root.right)
    return ans

ans = []
inorder(root)
print(f"ans ={ans}")

n =len(ans)

i = 1
j =0

while(i<n):

    if ans[j] > ans[i]:
        print("not a valid bst")
    i = i+1
    j = j+1

print("validbst")