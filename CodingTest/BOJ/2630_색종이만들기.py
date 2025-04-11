ans = [0, 0]

def find_paper(sz, start, end):
    global ans, paper
    
    cur = paper[0][0]
    fail = False
    for y in range(start, end):
        for x in range(start, end):
            if cur != paper[y][x]:
                fail = True
                break
        if fail:
            break
    
    if fail:
        if sz == 1:
            return
        n_sz = sz//2
        find_paper(n_sz, start+n_sz, end-n_sz)
        find_paper(n_sz, start, end-n_sz)
        find_paper(n_sz, start+n_sz, end)
        find_paper(n_sz, end-n_sz, end)
        
    else:
        ans[cur] += 1
    return 
    
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

find_paper(N, 0, N)
print(ans)