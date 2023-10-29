B =[
    [1,2],
    [2,3],
    [3,4],
    [4,5]
]

vertex  = set()

for each in B:
    vertex.add(each[0])
    vertex.add(each[1])

visted = [False]* len(vertex)

print(visted)