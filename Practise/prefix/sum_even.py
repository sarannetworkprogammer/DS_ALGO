
A = [1,2,3,4,5]

n = len(A)
p_sum_even = [None] * n
p_sum_even[0] = A[0]
print(p_sum_even)

for i in range(1,n):

    if i%2 == 0:
        p_sum_even[i] = p_sum_even[i-1] + A[i]
    else:
        p_sum_even[i] = p_sum_even[i-1]
    
print(f"even_indices_sum = {p_sum_even}")

B = [[0,3],[2,4]]
m = len(B)
out =[]

for i in range(0,m):
    l = B[i][0]
    r = B[i][1]

    if l == 0:
        ans = p_sum_even[r]
    else:
        ans = p_sum_even[r] - p_sum_even[l-1]
    
    out.append(ans)

print(f"out ={out}")


    
