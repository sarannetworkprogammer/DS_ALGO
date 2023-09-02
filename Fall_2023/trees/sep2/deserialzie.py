A  =[1,2,3,4,5,-1,-1,-1,-1,-1,-1]

n = len(A)
ans =[]

i = 0
j = 0

while (j<n):
    if A[j] != -1:
        A[i] = A[j]
        i = i+1
    else:
        A[j]=0
    j =j+1
print(A)

