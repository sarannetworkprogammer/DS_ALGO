def gcd(a,b):

    
    if a == 0 or b == 0:
        return a+b

    ans = 1
    n = min(a,b)

    for i in range(2,n+1):
        if (a%i==0 and b%i==0):
            ans = i
    return ans


ans = gcd(0,15)

print(f"ans ={ans}")