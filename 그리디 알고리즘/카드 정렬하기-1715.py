import heapq

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
hap = 0
while len(heap) > 1:
    result1 = heapq.heappop(heap)
    result2 = heapq.heappop(heap)
    hap += result1+result2
    heapq.heappush(heap, result1+result2)

print(hap)