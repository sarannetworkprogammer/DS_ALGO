A = [4, 3, 2, 6, 1]
k = 3
C = 11

n = len(A)
sum_val = 0
for i in range(0,k):
    sum_val = sum_val + A[i]
    s = 1
    e = k
    while (e < n):
        sum_val = sum_val - A[s-1] + A[e]
        if sum_val == C:
            print("exists =1")
            break
        e = e +1
        s = s+1
   
    

    

