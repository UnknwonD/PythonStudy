def btc(cur_sum, index, cnt):
    if index == n: # 마지막까지 순회한 경우 - 공집합은 존재하면 안됨
        return 1 if (cur_sum == s and cnt != 0) else 0
    # 합계에 포함하는 경우와, 그렇지 않은 경우를 return
    return btc(cur_sum + arr[index], index+1, cnt+1) + btc(cur_sum, index+1, cnt)
    
n, s = map(int, input().split())
arr = list(map(int, input().split()))

print(btc(0, 0, 0))