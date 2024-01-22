def gcd(a,b):

    if a  == 0 :
        return b
    return gcd(b%a , a)



ans = gcd(25,15)

print(f"ans ={ans}")

