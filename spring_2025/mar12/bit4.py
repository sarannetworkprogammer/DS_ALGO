A = [26,13,23,28,27,7,25]

ans = 0
n = len(A)

for b in range(30,-1,-1):
    cnt = 0
    for i in range(0,n):
        if ((A[i] >> b) & 1 == 1):
             
             cnt = cnt +1   
        
    if cnt >= 2:
        ans = ans | (1<<b)

        for i in range(0,n):
            if ((A[i] >> b) & 1 == 0):

                A[i] = 0


print(f"ans = {ans}")
        
                
            
    
    
        



print(f"ans ={ans}")
     
        



