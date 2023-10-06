from heapq import heappop, heappush, heapify

A = [1,3,2,3,3]

B = [5,6,1,3,9]

A = sorted(A)

n = len(A)
T = 0
heap =[]
heapify(heap)

for i in range(n):
    
    if T < A[i]:
        heappush(heap,B[i])
        T = T+1

    else:
        if B[i] > heap[0]:
            heappop(heap)
            heappush(heap,B[i])

print(f"heap ={heap}")
ans = sum(heap)

print(f"ans ={ans}")