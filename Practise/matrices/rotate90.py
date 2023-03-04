a = [[1,2,3],[4,5,6],[7,8,9]]
n = len(a)
m = len(a[0])

for i in range(0,n):
    for j in range(0,i):
        temp = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = temp

print(a)
for i in range(0,n):
    for j in range(0,(int(m/2))):
        tmp = a[i][j]
        a[i][j] = a[i][n-1-j]
        a[i][n-1-j] = tmp

print("after reversing\n")
print(a)
        