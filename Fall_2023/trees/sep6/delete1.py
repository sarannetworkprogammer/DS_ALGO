tmp = root

if temp.left == None and temp.right == None:
    # leaf node
    case1()

elif temp.left == None or temp.right == None:
    #node with one child
    case2()

else:
    #node with 2 children


def case1:
    #search the element with parent
    search(key,root)



def search(key,root):

    tmp = root

    while tmp != None:
        parent =tmp

        if tmp.val == key:
            break
            

        elif key > tmp.val:
            tmp = tmp.right
        else:
            tmp = tmp.left

    if parent.left.val == key:
        parent.left = None
    else:
        parent.right = None