
# Printing sub array topic

A = [2,8,9]

def print_subarray(start, end,A):
    print("subarray")
    for i in range(start,end+1):
        print(A[i])



# sum of the sub array

def sum_subarray(start, end,A):
    sum_sub = 0
    for i in range(start, end+1):
        sum_sub = sum_sub + A[i]
    print(f"sub_array_sum ={sum_sub}")

# Printing all possible sub arrays start end index  from 


def all_subarrays(A):
    n = len(A)

    for i in range(0,n):
        for j in range(0,n):
            print_subarray(i,j,A)

# Finding sum of each and every sub array

def sum_all_subarrays(A):
    n = len(A)
    for i in range(0,n):
        for j in range(i,n):
            sum_subarray(i,j,A)   # T.c O(N^3) because sum takes another O(n)



def main():
    A = [2,8,9]
    all_subarrays(A)
    sum_all_subarrays(A)





if __name__ == "__main__":
    main()
