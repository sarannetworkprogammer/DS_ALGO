A = [4,5,2,10,12]

n = len(A)
ans = [-1]*n
for i in range(n):
    for j in range(i+1,n):
        if A[j] > A[i]:
            ans[i] = A[j]
            break
print(ans)
