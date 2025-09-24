n, m = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

start, end = 1, house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    # 앞집부터 하나씩 설치
    for h in house:
        cnt += 1
        next = h + mid
    
    if next >= mid: