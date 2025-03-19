nums = [1,2,3,4,4,3,2,1]

n = len(nums)
k = int(n/2)
out1 = []
out2  = []
out3 = []

for i in range(0,k):
    out1.append(nums[i])

for i in range(k,n):
    out2.append(nums[i])

print(f"out1 = {out1}")
print(f"out2 = {out2}")

for i in range(0,k):
    out3.append(out1[i])
    out3.append(out2[i])

print(f"out3 ={out3}")