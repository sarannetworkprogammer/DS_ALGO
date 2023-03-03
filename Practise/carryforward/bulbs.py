A = [0,1,0,1]

n =len(A)

count = 0
def check(A):
    n = len(A)
    count = 0
    for i in range(0,n):
        count = count + 1
        if A[i] == 0:
            for i in range(i,n):
                if A[i] == 0:
                    A[i] =1
                else:
                    A[i] = 0
    print(count)


check(A)

"""  
    total = 0
    for each in A:
        total = total +each
    if total != n:
        count = count + 1 
        check(A)
    return count
        
count =check(A)


print(count)

"""