import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    M = int(sys.stdin.readline())
    left = []
    right = []
    cnt = 0
    ans = []
    for _ in range(M//10 + 1):
        N = list(map(int, sys.stdin.readline().split()))
        
        for i in range(len(N)):    
            if len(left) == 0 or -left[0] >= N[i]:
                heapq.heappush(left, -N[i])
            else:
                heapq.heappush(right, N[i])
            
            if len(left) > len(right) + 1:
                tmp = -heapq.heappop(left)
                heapq.heappush(right, tmp)
            elif len(right) > len(left):
                tmp = heapq.heappop(right)
                heapq.heappush(left, -tmp)
                
            cnt += 1
            if cnt % 2 != 0:
                ans.append(-left[0])
    
    print(len(ans))        
    for i in range(len(ans)):
        print(f'{ans[i]} ', end='')
        if ((i+1) % 10) == 0:
            print('')
    print('')