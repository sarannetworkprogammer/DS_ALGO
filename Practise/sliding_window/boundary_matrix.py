A =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]


i = 0
j =0

n = len(A)

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


