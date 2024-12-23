n = int(input())

dp = {1: 0}

def memo(cur):
    if cur in dp.keys():
        return dp[cur]
    
    if (cur % 3 == 0) and (cur % 2 == 0):
        dp[cur] = min(memo(cur//2)+1, memo(cur//3)+1)
    elif (cur % 3 == 0):
        dp[cur] = min(memo(cur//3)+1, memo(cur-1)+1)
    elif (cur % 2 == 0):
        dp[cur] = min(memo(cur//2)+1, memo(cur-1)+1)
    else:
        dp[cur] = memo(cur-1)+1
        
    return dp[cur]


print(memo(n))