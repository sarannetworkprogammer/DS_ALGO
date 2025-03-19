num = [1,2,0,0]
k = 34

s =""

for each in num:
    s = s + str(each)

s = int(s) + k
print(f"s ={s}")

s = str(s)
print(f"s ={s}")
out = []
for each in s:
    out.append(int(each))

print(out)
