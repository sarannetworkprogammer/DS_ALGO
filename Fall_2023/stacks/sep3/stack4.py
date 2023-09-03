A = [4,5,2,10,12]

n = len(A)
print(f"n={n}")

ans = [-1]*n
print(f"ans ={ans}")

stack = []
stack.append(A[n-1])

i = n-2

for i in range(n-2,-1,-1):

    while len(stack) != 0 and stack[-1] <= A[i]:

        stack.pop()

    if stack:
        ans[i] = stack[-1]
    
    stack.append(A[i])

print(f"final_answer={ans}")
