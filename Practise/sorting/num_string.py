
A = [3, 30, 34, 5, 9]

A = list(map(str,A))

print(f"after conversion to strings= {A}")


from functools import cmp_to_key

def comparator(num1,num2):
    if (num1+num2 > num2+num1):
        return -1
    else:
        return 1+

A = sorted(A,key=cmp_to_key(comparator))

if A[0]==0:
    print("0")

print("".join(A))


