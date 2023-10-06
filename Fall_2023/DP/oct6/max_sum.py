A  = [[74,37,82,1],[66,38,16,1]]

n = len(A[0])

B = []

print(f"n = {n}")

B.append(max(A[0][0],A[1][0]))

for i in range(1,n):
    temp = max(A[0][i], A[1][i])
    B.append(temp)

print(f"B ={B}")


res = [None]*n

res[0] = B[0]
res[1] = max(B[0],B[1])


for i in range(2,n):
    res[i] = max(res[i-1], res[i-2]+B[i])


print(f"res= {res}")

print(f"max_val ={max(res)}")

