A =[[3,2],[2,3]]

n = len(A)
print("n=",n)

m = len(A[0])

print(f"m={m}")

i =0
j =m-1

print(f"j={j}")

sum_val =0

while (i<n) and(j>=0):

  

        #print(i,j)

    sum_val = sum_val + A[i][j]
    print("sum_val",sum_val)

    i = i+1
    j = j-1

print(sum_val)


