class TreeNode:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def pre_order(root):
    answer = []

    pre_order_traversal(root,answer)

    return answer

def pre_order_traversal(root,answer):

    if root is None:
        return
    
    answer.append(root.val)
    pre_order_traversal(root.left,answer)
    pre_order_traversal(root.right,answer)

    return







root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(pre_order(root))