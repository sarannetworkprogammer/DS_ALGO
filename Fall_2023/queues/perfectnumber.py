"""
11,22,1111
"""
A =10

from collections import deque

if A == 1:
    print("1")

if A == 2:
    print("2")

q = deque()
q.append("1")
q.append("2")

#print(f"q= {q}")
#print(f"type_q= {type(q)}")

while True:
    temp = q.popleft()

    q.append(temp+"1")

    count = count +1
    if count == A:
        ans = temp +"1"
        break
    q.append(temp+"2")
    count = count +1
    if count == A:
        ans = temp + "2"

    
