A = [1,2,3]

n = len(A)

ans = 0
MOD = int(1e9 + 7)

for i in range(0,n):
    for j in range(0,n):
        ans = (ans + ((A[i]% A[j]) % MOD)) % MOD


print(ans)