A = 5
B = [
    [1,2],
    [4,1],
    [2,4],
    [3,4],
    [5,2],
    [1,3]
]

vertex = set()
for each in B:
    vertex.add(each[0])
    vertex.add(each[1])

print(f"vertex = {vertex}, num_vertices = {len(vertex)}, edges = {len(B)}")

from collections import deque

graph = {} 

for edge in B:

    if edge[0] not in graph:
        graph[edge[0]] = []
    
    graph[edge[0]].append(edge[1])
    

print(f"graph ={graph}")


visited = set()

queue  = deque([1])

while queue:

    current_vertex = queue.popleft()

    if current_vertex == A:
        print("Found")
    
    if current_vertex in visited:
        continue

    if current_vertex in graph:
        for neighbor in graph[current_vertex]:
            print(neighbor)
            queue.append(neighbor)

        visited.add(current_vertex)

print("not route")




# This is Bfs approach to solve the problem While level order traveseral we follow queue approach