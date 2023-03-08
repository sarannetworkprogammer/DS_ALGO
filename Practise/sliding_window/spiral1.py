
n =5

val = 1
i=0
j=0
cols =5
rows =5
mat = matrix = [[0 for _ in range(cols)] for _ in range(rows)]

while (n > 1):
    for k in range(0,n-1):
        mat[i][j] = val
        val = val +1
        j = j+1

    for k in range(0,n-1):
        mat[i][j] = val
        val = val +1
        i =i+1
    for k in range(0,n-1):
        mat[i][j] = val
        val = val +1
        j = j-1


    for k in range(0,n-1):
        mat[i][j] = val
        val = val +1
        i = i-1
    i = i+1
    j = j+1
    n = n-2

if n == 1:
    mat[i][j] = val


for each in mat:
    print(each)