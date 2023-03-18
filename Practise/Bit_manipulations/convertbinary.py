A =4
B=2

def decimaltoanybase(A,B):
    ans =[]

    while (A>0):
        temp = A%B
        print(temp,end="")
        ans.append(temp)
        A = int(A/B)
        #print(A)

    print(ans)
    n = len(ans)
    out =0

    i = n-1
    t =""
    

    while(i>=0):
        #print(ans[i],end="")
        t = t+ str(ans[i])
        i = i-1

    return int(t)

number = decimaltoanybase(A,B)
print(f"number={(number)}")





