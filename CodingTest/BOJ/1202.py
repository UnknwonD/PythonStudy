import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())

items = sorted([[*map(int, input().split())] for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])

res, tmp = 0, []
for bag in bags:
    while items and items[0][0] <= bag:
        heapq.heappush(tmp, -items[0][1])
        heapq.heappop(items)
    
    if tmp:
        res -= heapq.heappop(tmp)

print(res)