count_good =0

A = [3,16,16,15,9,16,2,7,6,17,3,9]
B = 65


def sum_subarray(start, end,A):
    sum_sub = 0
    for i in range(start, end+1):
        sum_sub = sum_sub + A[i]
    return sum_sub


def all_subarrays(A,count_good):
    n = len(A)

    for i in range(0,n):
        for j in range(i,n):
            sum_sub = sum_subarray(i,j,A)
            if (((j-i+1)%2 == 0))and (sum_sub < B):
                count_good = count_good + 1
            elif (((j-i+1)%2 == 1)) and (sum_sub > B):
                count_good = count_good + 1
            else:
                pass
    return count_good


ans =all_subarrays(A,count_good)
print(f"count_good ={ans}")
