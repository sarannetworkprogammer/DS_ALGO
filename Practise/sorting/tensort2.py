from functools import cmp_to_key

A = [2, 24, 22, 19]

def compare(num1,num2):
    
    if num1 >= 10:
        a = (num1/10)%10
    else:
        a =0

    if num2 >= 10:
        b = (num1/10)%10
    else:
        b =0

    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        if num1 < num2:
            return 1
        else:
            return -1

A = sorted(A,key=cmp_to_key(compare))

print(A)