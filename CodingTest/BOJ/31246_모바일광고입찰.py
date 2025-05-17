import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = 0

other = []
trigger = 0
for i in range(N):
    a, b = map(int, input().split())
    
    if a < b:
        other.append(b - a)
    else:
        trigger += 1

other.sort()
while trigger < K:
    cur = other.pop(0)
    trigger += 1
    ans = max(cur, ans)
print(ans)