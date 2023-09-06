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

"""-------------------inserting 14 in bst"""


def insert(root,key):

    tmp = root

    parent = TreeNode(None)
   
    while (tmp != None):
        parent = tmp

        if tmp.val == key:
            print("val is already there")
        elif key > tmp.val:
            tmp = tmp.right
        else:
            tmp = tmp.left


    if key < parent.val:
        parent.left = TreeNode(key)
    else:
        parent.right = TreeNode(key)
key = 14
insert(root,key)

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

