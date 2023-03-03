list2=[]
def print_subarray(start, end,A):
    list1 = []
    for i in range(start,end+1):
        list1.append(A[i])
    list2.append(list1)
    print(list2)
       

def all_subarrays(A):
    n = len(A)

    for i in range(0,n):
        for j in range(i,n):
            print_subarray(i,j,A)


def main():
    A = [2,8,9]
    list2 =[]
    all_subarrays(A)


if __name__ == "__main__":
    main()