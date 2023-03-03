A = [2,2,6,4,5,1,5,2,6,4,1]

n = len(A)

max_val = max(A)
min_val = min(A)

print(f"min_val = {min_val}")
print(f"max_val ={max_val}")
ans = n

last_min_index = -1
last_max_index = -1

for i in range(0,n):
    if A[i] == max_val:
        last_max_index = i
        if last_min_index != -1:
            ans = min(ans, (abs(last_max_index - last_min_index) + 1))
    
    elif A[i] == min_val:
        last_min = i
        if last_max_index != -1:
            ans =  min(ans, (abs(last_max_index - last_min_index) + 1))
        


print(ans)


