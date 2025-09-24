import heapq
n = int(input())

ans = 0
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

while cards:
    cur = 0

    if len(cards) >= 2:
        for i in range(2):
            cur += heapq.heappop(cards)
        ans += cur
        heapq.heappush(cards, cur)
    else:
        break

print(ans)