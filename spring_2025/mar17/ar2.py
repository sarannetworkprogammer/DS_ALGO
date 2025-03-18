A = [1,2,3,4]

n = len(A)

k = int(n/2)

B = []
C = []

for i in range(0,k):
    B.append(A[i])

for i in range(k,n):
    C.append(A[i])

print(f"B ={B}")

print(f"C = {C}")