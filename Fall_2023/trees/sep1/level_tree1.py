from collections import deque

q = deque()

q.append("a")
q.append("b")
q.append("c")

print(f"initial queue ={q}")

print(q.popleft())

print(f"after removing one element ={q}")