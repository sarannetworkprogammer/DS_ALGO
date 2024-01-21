string = "ABC"
n = len(string)

a = list(string)

print(f" a ={a}")

v


def permute(a,l,r):

    if l == r:
        print(tostring(a))

    else:

        for i in range(l,r):

            a[l], a[i] = a[i],a[l]

            permute(a,l+1,r)
            a[l],a[i] = a[i] ,a[l]
           
