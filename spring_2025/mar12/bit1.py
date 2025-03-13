A = [1,2,1,2,3]

ans =0
n = len(A)

for i in range(0,n):
    ans = ans ^ A[i]

print(ans)


# T.C : O(n)
# s.c : O(1)
