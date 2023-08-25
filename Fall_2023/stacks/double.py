s ="abbccd"

stack =[]

for c in s:
    if stack:
        if c not in stack[-1]:
            stack.append(c)
    
        else:
            stack.pop()
    else:
        stack.append(c)

ans = ""

for each in stack:
    ans = ans+ each

print(f"ans ={ans}")

