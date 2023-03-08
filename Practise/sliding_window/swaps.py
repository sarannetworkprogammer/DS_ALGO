A =[25,30,2,18,7,6,9,3,50]


B = 100
n = len(A)
k =0

for i in range(0,n):
    if A[i] <= B:
        k = k+1


print(f"k={k}")

if (k==0) or (k == 1):
    print("0")

bad = 0
for i in range(0,k):
    if A[i] > B:
        bad = bad +1

ans = bad
s =1
e =k

while(e<n):

    if (A[s-1]>B):
        bad = bad-1
    if (A[e]>B):
        bad = bad +1

    if (bad < ans):
        ans = bad



    s= s+1
    e= e+1
    print(f"ans={ans}")