class TreeNode:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def inordertraversal(root):
    answer = []

    inordertraversalutil(root,answer)
    return answer
    
def inordertraversalutil(root,answer):

    if root is None:
        return
    inordertraversalutil(root.left,answer)
    answer.append(root.val)
    inordertraversalutil(root.right,answer)
    return






root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inordertraversal(root))