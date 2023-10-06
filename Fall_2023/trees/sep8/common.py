    def test():
        
        def solve(self, A, B):

        out1 = []
        out2 = []

        def traversal(root):

            if root is None:
                return
            traversal(root.left)
            out1.append(root.val)
            traversal(root.right)

        
        def traversal_b(root):

            if root is None:
                return
            traversal_B(root.left)
            out2.append(root.val)
            traversal_b(root.right)


        
        
        traversal(A)
        traversal_b(B)

        common = []

        for each in out1:
            if each in out2:
                common.append(each)

        sum_val = sum(common)

        if len(common) == 0:
            return 0
       else:
           return sum_val %(10**9 + 7)