import heapq

n, k = map(int, input().split())
MAX = 200001  # upper bound

INF = float('inf')
dists = [INF] * MAX
heap = [(0, n)]  # (time, position)

while heap:
    time, pos = heapq.heappop(heap)
    
    if pos == k:
        print(time)
        break

    if dists[pos] <= time:
        continue

    dists[pos] = time

    if pos * 2 < MAX and dists[pos * 2] > time:
        heapq.heappush(heap, (time, pos * 2))
    
    for next_pos in (pos - 1, pos + 1):
        if 0 <= next_pos < MAX and dists[next_pos] > time + 1:
            heapq.heappush(heap, (time + 1, next_pos))
    