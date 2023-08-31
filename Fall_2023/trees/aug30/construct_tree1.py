
def construct(inorder,postorder,isi, iei, psi,pei):

    if isi > iei:
        return None
    
    dict1 = {}

    for i in range(len(inorder)):
        dict1[inorder[i]] = i

    
    root = TreeNode(postorder[pei])

    idx = dict1[root]

    count_l = idx-isi
    
    root.left = construct(inorder,postorder,isi,idx-1,psi, psi+count_l-1)
    root.right = construct(inorder,postorder,idx+1,iei,psi+count_l, pei-1)

    return root



    

    





