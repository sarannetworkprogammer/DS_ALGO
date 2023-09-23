#peek of binary heap which is root of the heap
## return list[1]


class Heap:

    def __init__(self,size):
        self.customList = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = size +1

def peekofHeap(rootNode):

    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.

def levelordertraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])




newBinaryHeap = Heap(5)
print(sizeofHeap(newBinaryHeap))