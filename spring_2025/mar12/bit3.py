A = [9,11,9,8,10,11]

xor = 0

n = len(A)
for i in range(0,n):
    xor = xor ^ A[i]

print(f"xor = {xor}")

b = -1

for i in range(0,32):
    if (xor >> i) & 1 == 1:
        b = i
        break

print(f"b={i}")

x = 0
y = 0

for i in range(0,n):
    if ((A[i] >> b) & 1 == 1):
        
        x = x ^ A[i]
    else:

        y = y ^ A[i]

print(f"x= {x}")
print(f"y = {y}")