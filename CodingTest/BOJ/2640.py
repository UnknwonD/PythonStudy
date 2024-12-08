def count_color(cur, length, color):
    start = cur
    end = (cur[0] + length-1, cur[1] + length-1)

    now = graph[start[0]:end[0]][start[1]:end[1]]

    cnt = 0
    for row in now:
        for col in row:
            if col == color:
                cnt += 1
    
    if length**2 == cnt:
        return 1
    else:
        # 4등분으로 나눠서 return
        return count_color(cur, length//2, color) + count_color(cur, length//2, color) + count_color(cur, length//2, color) + count_color(cur, length//2, color)


n = int(input())

paper = []

for _ in range(n):
    line = list(map(int, input().split()))
    paper.append(line)

