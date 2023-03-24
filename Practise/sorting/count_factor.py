def count_factor(n):

    cnt_factors =0

    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if (i*i ==n):
                cnt_factors =cnt_factors +1
            else:
                cnt_factors = cnt_factors + 2
       

    return cnt_factors


A = [ 36, 13, 13, 26, 37, 28, 27, 43, 7 ]
B=  [  9, 2, 2, 4, 2, 6, 4, 2, 2]
B=[]


for i in range(len(A)):
    B.append(count_factor(A[i]))

print(B)