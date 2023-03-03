A = [2,1,3,4,5]


def sum_subarray(start, end,A):
    sum_sub = 0
    for i in range(start, end+1):
        sum_sub = sum_sub + A[i]
    return sum_sub


def prefix_sum(A):
    p_sum = list()
    p_sum.append(A[0])
    n = len(A)

    for i in range(1,n):
        p_sum[0] = A[0]
        p_sum[i] = p_sum[i-1] + A[i]
       
    print(p_sum)

def all_subarrays(A):
    n = len(A)
    total_sum =0
    max_sum =0
    

    for i in range(0,n):
        for j in range(i,n):
            sum_sub = sum_subarray(i,j,A)
            #print(sum_sub)
            if (sum_sub > max_sum) and (sum_sub <= 12):
                max_sum = sum_sub

    print(f"max_sum ={max_sum}")
     


all_subarrays(A)
prefix_sum(A)