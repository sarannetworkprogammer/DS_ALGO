def cnt(n):
    return ((n*(n+1)) // 2)

 A = [1, 2, 3, 4, 5]
MOD = int(1e9 + 7)

ans = 0
n = len(A)

for b in range(0,27):
    c = 0
    # total number of subarray of an array of size n

    C = cnt(n)

    for i in range(n):
        if A[i] & 1:
            C = c - cnt(c)
            c= 0
        else:
            c = c+1
        A[i] >> 1
    
    C = C - cnt(c)
