A = [1, 2, 3]

n = len(A)
ans = 0
for i in range(0,n-1):
    for j in range(i+1, n):
        ans = ans + (A[i] ^ A[j])

print(f"ans ={ans}")
        