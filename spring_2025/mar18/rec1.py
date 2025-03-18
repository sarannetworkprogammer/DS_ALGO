# Recursion

def sum(n):

    if n == 1:
        return 1

    return (n + sum(n-1))


ans = sum(5)

print(f"ans ={ans}")