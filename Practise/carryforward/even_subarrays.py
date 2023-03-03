
A = [2,4,8,6,7,6]

def print_subarray(start, end,A):
    list1 = []
    for i in range(start,end+1):
        list1.append(A[i])

    if (list1[0] % 2 != 0) and (list1[-1] % 2 !=0):
        return "NO"
    




    
def all_subarrays(A):
    n = len(A)

    for i in range(0,n):
        for j in range(i,n):
            ans = print_subarray(i,j,A)
            if ans == "NO":
                return "NO"

    return "YES"



print(all_subarrays(A))
