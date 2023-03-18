# T.C is O(n) and s.c is o(n)

A = [1,2,3,4,5]
def prefix_odd_sum(A):
    n = len(A)
    p_sum_odd = [None] * n
    p_sum_odd[0] = 0
    for i in range(1,n):
        if i%2 == 1:
            p_sum_odd[i]= p_sum_odd[i-1] + A[i]
        else:
            p_sum_odd[i] = p_sum_odd[i-1]

    return p_sum_odd


if __name__ == "__main__":
    
    odd_sum = prefix_odd_sum(A)
    print(f"oddsum ={odd_sum}")
