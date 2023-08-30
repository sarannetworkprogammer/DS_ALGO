class TreeNode:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def post_order(root):

    answer = []

    post_order_util(root,answer)
    return answer

def post_order_util(root,answer):

    if root is None:
        return

    post_order_util(root.left,answer)
    post_order_util(root.right,answer)
    answer.append(root.val)
    return



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print(f"post_order = {post_order(root)}")