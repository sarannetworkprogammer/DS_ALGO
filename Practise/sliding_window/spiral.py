A =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

n = len(A)

i =0
j=0

while (n>1):

    for k in range(0,n-1):
        print(A[i][j])
        j = j +1

    for k in range(0,n-1):
        print(A[i][j])
        i = i + 1

    for k in range(0,n-1):
        print(A[i][j])
        j = j - 1

    for k in range(0,n-1):
        print(A[i][j])
        i = i-1

    i =i +1
    j = j+1
    n = n-2

if n==1:
    print(A[i][j])