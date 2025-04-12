ans = [0, 0]

def find_paper(sz, row, col):
    global ans, paper
    
    fail = False
    start_row = max(0, row-sz)
    start_col = max(0, col-sz)
    cur = paper[start_row][start_col]
    
    if sz == 1:
        ans[cur] += 1
        return
    
    for y in range(start_row, row):
        for x in range(start_col, col):
            now = paper[y][x]
            if cur != paper[y][x]:
                fail = True
                break
        if fail:
            break
    
    if fail:
        n_sz = sz//2
        
        # 분할 시작 (행, 열)
        find_paper(n_sz, start_row + n_sz, start_col + n_sz)
        find_paper(n_sz, start_row + n_sz, col)
        find_paper(n_sz, row, start_col + n_sz)
        find_paper(n_sz, row, col)
    else:
        ans[cur] += 1
    return 
    
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

find_paper(N, N, N)

for a in ans:
    print(a)