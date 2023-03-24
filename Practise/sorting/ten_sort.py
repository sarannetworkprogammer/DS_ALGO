

def comparator(num1,num2):

    if len(str(num1)) >=2:
        a = (str(num1))[-2]
    else:
        a =0
    if len(str(num2)) >= 2:
        b = (str(num2))[-2]
    else:
        b=0

    if int(a) < int(b):
        return -1
    
    elif int(a) > int(b):
        return 1

    else:
        if num1 > num2:
            return 1
        else:
            return -1

result = comparator(32,45)

print(result)