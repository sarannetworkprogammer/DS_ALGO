A = [4, 5, 2, 10, 8]

stack =[]

n = len(A)

ans =[0]*n
ans[n-1] = -1
stack.append(A[n-1])

print(f"initial_stack={stack}")
print(f"initia_ans =")


for i in range(n-2,-1):

    while len(stack) != 0 and stack[-1] <= A[i]:
        stack.pop()
    
    
    if stack:
        ans[i] = stack[-1]
    else:
        ans[i] =-1

    stack.append(A[i])
print(ans)