import sys

N = int(sys.stdin.readline())
fear = list(map(int, sys.stdin.readline().split()))

fear = sorted(fear) # 정렬

groups = 0
cur = []
for f in fear: # 공포도 순회 (낮은것부터 넣으면 그룹 최대화 가능)
    cur.append(f)
    
    # 그룹에 넣어도 되는지 확인하고 초기화
    if cur[-1] <= len(cur):
        groups += 1
        cur = []

print(groups)
