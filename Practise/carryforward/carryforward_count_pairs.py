
A = ['c','a','g','g','a','a','g']

ans =0
count_a =0
n = len(A)

for i in range(0,n):
    if A[i] == "a":
        count_a = count_a + 1

    elif A[i] == "g":

        ans = ans + count_a

print(ans)