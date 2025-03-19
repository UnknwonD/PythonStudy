import sys
import heapq

n = int(sys.stdin.readline())
left_heap = []
right_heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if len(left_heap) == 0 or -left_heap[0] >= x:
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)
        

    if len(right_heap) + 1 < len(left_heap):
        tmp = -heapq.heappop(left_heap)
        heapq.heappush(right_heap, tmp)
    elif len(right_heap) > len(left_heap):
        tmp = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -tmp)
    
    print(-left_heap[0])
        
