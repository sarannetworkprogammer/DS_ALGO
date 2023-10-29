

def (bfs,)

visited = set()
visited.add(B[0][0])

queue = deque(B[0][0])

while queue:
    current_vertex = queue.popleft()
    if current_vertex == A:
        print("True")
        break
     