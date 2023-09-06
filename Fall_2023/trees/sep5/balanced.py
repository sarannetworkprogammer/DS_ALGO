class TreeNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(5)

root.left = TreeNode(9)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)



class Solution:

    def isBalanced(self,root):


        def dfs(root):

            if not root:
                return [True,0]

            left = dfs(root.left)
            right= dfs(root.right)

            balanced = (left[0] and right [0] and abs(left[1]-right[1]) <=1)

            return [balanced, 1+max(left[1],right[1])]

        return dfs(root)[0]

