
A = 1111
B = 2
A = str(A)
n = len(A)
j = n -1
ans =0
for i in range(0,n):
    ans = ans + int(A[j])*B**i

    j = j-1

print(ans)

