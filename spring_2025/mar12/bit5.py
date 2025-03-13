A =[1,2,3,7,5]


ans = A[0] ^ A[1]


n = len(A)

i = 1
j = i+1
while( i < n-1):
    print(f"i={i}, j ={j}")
    ans = min(ans, A[i]^A[j])
    i = i + 1
    j = j +1

print(f"ans = {ans}")
  