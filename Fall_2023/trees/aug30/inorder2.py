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

def print_tree(root):

    if root is not None:
        print(root.val, end=" , ")
        print_tree(root.left)
        print_tree(root.right)

print_tree(root)