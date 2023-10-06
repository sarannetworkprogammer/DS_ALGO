A = 5

ways = [None] *(A+1)

print(f"length = {len(ways)}")

print(f"ways ={ways}")

ways[0]= 0
ways[1] =1
ways[2] =2

print(f"ways= {ways}")

for i in range(3,A+1):
    print(f"i = {i}")

    ways[i] = ways[i-2] + ways[i-1]

print(f"ways= {ways}")