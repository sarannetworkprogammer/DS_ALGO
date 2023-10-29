from collections import deque
A = 5
B =[
    [1,2],
    [2,3],
    [3,4],
    [4,5]
]

vertex = set()
print(len(B))

queue = deque([])

queue.append(B[0][0])
queue.append(B[0][1])

print(f"queue = {queue}")
print(f"vertex ={vertex}, number= {len(vertex)}")


for each in B:
    vertex.add(each[0])
    vertex.add(each[1])


for i in B[1:]:
    print(i[1])


count =1

while queue:

    current_vertex = queue.popleft()

    print(f" {count}-- {current_vertex}")
    
    for i in B[1:]:
        if current_vertex == i[0]:
            queue.append(i[1])
  

    print(queue)
    if current_vertex == A:
        print("true--------found")
        break
