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


def heapifyTreeInsert(rootNode,index,heapType):

    parentIndex = int(index/2)

    if index <=1:
        return
    
    if heapType == "Min":
    
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp

        heapifyTreeInsert(rootNode,parentIndex,heapType)

    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp

        heapifyTreeInsert(rootNode,parentIndex,heapType)


def insertnode(rootnode,nodevalue, heaptype):

    if rootnode.heapsize + 1 == rootnode.maxsize:
        return "The Binary Heap is full"
    
    rootnode.customlist[rootnode.heapsize+1] = nodevalue
    rootnode.heapsize +=1
    heapifyTreeInsert(rootNode,rootNode.heapsize,heaptype)
    return "The value has been successfully inserted"








newBinaryHeap = Heap(5)
print(sizeofHeap(newBinaryHeap))