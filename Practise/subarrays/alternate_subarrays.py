
A = [0, 0, 0, 1, 1, 0, 1]
B = 1
def get_subarray(start,end,A):
    count =0
    serch = A
    search = A[start]
    for i in range(start+1,end+1):
        if A[i] == 1-search:
            search = A[i]
            count = count +1
    if count == end-start:
        index = (start+end)/2
    return int(index)
    
    



        


def get_all_subarray(A,B):
    n = len(A)
    index = -1
    mid_index =[]
    for i in range(0,n):
        for j in range(i,n):
            if (j-i+1 == B):
                index = get_subarray(i,j,A)
                mid_index.append(index)
    print(mid_index)

# check alternate elements

get_all_subarray(A,B)