a = [[1,2,3],[4,5,6],[7,8,9]]
n = len(a)

for i in range(0,n):
    for j in range(0,i):
        temp = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = temp


print(a)

