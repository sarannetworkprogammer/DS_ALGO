stack =[]

A = ["2","1","+","3", "*"]

operands = ["+","-","/","*"]

def evaluate(op1,op2, t):

    if t == "+":
        return int(op1) + int(op2)

    elif t == "-":
        return int(op1)-int(op2)

    elif t == "/":
        return int(op1)/int(op2)

    else:
        return int(op1) * int(op2)


n = len(A)

for i in range(n):
    if A[i] not in operands:
        stack.append(A[i])

    else:
        op2 = stack.pop()
        op1 = stack.pop()
        res = evaluate(op1,op2,A[i])
        stack.append(res)

print(stack[0])


