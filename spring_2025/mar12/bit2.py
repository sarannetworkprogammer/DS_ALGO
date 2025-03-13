A = [2,1,3,1,2,1,2]

n = len(A)

print(f"n ={n}")

ans = 0

for i in range(0,32):
    cnt = 0
    for j in range(0,n):
        if (A[j]>>i) & 1 == 1:
            cnt = cnt + 1
    if cnt %3 == 1:
        ans = ans | (1<<i)

print(f"ans = {ans}")
# T.C = O(n)

#s.c = O(1)