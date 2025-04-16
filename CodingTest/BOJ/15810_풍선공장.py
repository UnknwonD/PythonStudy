N, M = map(int, input().split())
staff = [*map(int, input().split())]

start, end = 0, max(staff)*M
ans = 0
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for s in staff:
        cnt += mid // s
        
    if cnt >= M:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)