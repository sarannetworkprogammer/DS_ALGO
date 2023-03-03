

A =[2,1,3,4,5]
n = len(A)
max_sum =0

def prefix_sum(A):
   
    p_sum = [None] * len(A)
    p_sum[0]= A[0]
    for i in range(1,n):
        p_sum[i] = p_sum[i-1] + A[i]
    
    return p_sum
p_sum = prefix_sum(A)

for i in range(0,n):
    for j in range(i,n):
        if (i == 0):
            sub_sum = p_sum[j]
        else:
            sub_sum = p_sum[j]-p_sum[i-1]
        if (sub_sum > max_sum) and (sub_sum <= 12):
            max_sum = sub_sum



print(f"max_sum ={max_sum}")





