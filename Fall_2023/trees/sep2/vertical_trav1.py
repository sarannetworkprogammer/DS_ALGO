from collections import deque
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

vl =0
root_pair = (root,vl)

print(f"pair = {root_pair}")

q = deque()

q.append(root_pair)

dict1 = {}
max_vl = 0
min_vl = 0

node = print(f"root_Val={root_pair[0].val}")
             
vl = print(root_pair[1])



while q:

    print("each iteration")

    pair_rp = q.popleft()
    node = pair_rp[0]
  
    
    vl = pair_rp[1]
    print(f"node_val ={node.val}")
    print(f"vl ={vl}")
    min_vl = min(min_vl, vl)
    
    max_vl = max(max_vl,vl)

  
    if vl not in dict1:
        dict1[vl] = [node.val]
    else:
        dict1[vl].append(node.val)

        
    if node.left:
        q.append((node.left,vl-1))
    if node.right:
        q.append((node.right,vl+1))

print(f"min_val ={min_vl} max_val ={max_vl}")

print("values")
ans =[]
for i in range(min_vl,max_vl+1,1):
    ans.append(dict1[i])

print(ans)

#top view of tree
ans2 =[]
for i in range(min_vl,max_vl+1,1):
    ans2.append(dict1[i][0])

print(f"ans2 ={ans2}")
