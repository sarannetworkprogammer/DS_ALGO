
A = [20,3,13,5,10,14,8,5,11,9,1,11]
B = 9

n = len(A)
print(n)

sum_val = 0

for i in range(0,B):
    sum_val = sum_val + A[i]

min_val = (sum_val/B)

print(f"first_average_val ={min_val} ")

s =1
e =B
sub_index =0

while(e<n):

    sum_val = sum_val -A[s-1] + A[e]
    avg = (sum_val/B)

    print(f"{s} th avg={avg}")

    if min_val > avg:
        min_val = avg
        sub_index = s
        print(f"sub_index ={sub_index}")
    
    e = e+1
    s= s+1


