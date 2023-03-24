A = [ 3, 0, 9, 7, 8 ]

A = sorted(A,reverse=True)

print(A)

sum_val = 0

n = len(A)

for i in range(0,n):
    sum_val = sum_val +A[i]

cost =sum_val

print(f"first= {cost}")
temp =0

for i in range(1,n):
    sum_val = sum_val -A[i-1]
    print
    print(temp)
    cost = cost + sum_val
    print("iteration")
    print(cost)
