
A = [2,9,5]


def sum_subarray(start, end,A):
    sum_sub = 0
    for i in range(start, end+1):
        sum_sub = sum_sub + A[i]
    return sum_sub

def all_subarrays(A):
    n = len(A)
    total_sum =0

    for i in range(0,n):
        for j in range(i,n):
            sum_sub = sum_subarray(i,j,A)
            total_sum = total_sum +sum_sub
    print(total_sum)

def sum_contribution(A):
    ans = 0
    n = len(A)
    for i in range(0,n):
        ans = ans + A[i] *(i+1)*(n-i)
    print(f"ans={ans}")

all_subarrays(A)
sum_contribution(A)