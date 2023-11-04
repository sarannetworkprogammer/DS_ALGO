A = 5
B = [
    [1,2],
    [4,1],
    [2,4],
    [3,4],
    [5,2],
    [1,3]
]

graph = {}

for edge in B:

    if edge[0] not in graph:
        graph[edge[0]] = []
    graph[edge[0]].append(edge[1])

print(f"graph ={graph}")

visited = set()

stack = [1]

count = 0

visited = set()

while stack:


    count = count + 1

    if count == 5:
        break

    current_vertex = stack.pop()
    print(f"current_vertex = {current_vertex}")

    if current_vertex in visited:
        print("cycle")

    if current_vertex in graph:
        for neigbor in graph[current_vertex]:
            print(f"neigbor ={neigbor}")
            stack.append(current_vertex)
    
    visited.add(current_vertex)
    


print("no cycle found")