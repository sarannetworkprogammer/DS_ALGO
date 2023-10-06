from heapq import heappop, heappush, heapify

heap =[]
heapify(heap)

heappush(heap,10)
heappush(heap,20)
heappush(heap,30)
heappush(heap,400)

print(f"heap ={heap}")


heappop(heap)
heapify(heap)

print(f"after_removing={heap}")

