n = int((input()))
times = list(map(int, input().split()))
times.sort()

ans, sum_time = 0, 0
for time in times:
    ans += sum_time + time
    sum_time += time

print(ans)