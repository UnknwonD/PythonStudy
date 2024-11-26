# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# def btc(cur, cur_sum, index):
#     if index == len(arr):
#         return 1 if cur_sum == m else return 0
#     else:
#         next_arr = cur + list(arr[index])
#         next_sum += arr[index]
        
#         return btc(next_arr, next_sum, index+1) + btc(cur, cur_sum, index+1)

# print(btc([], 0, 0))

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def btc(cur_sum, index):
    if index == len(arr):  # 종료 조건: 배열 끝까지 탐색했을 때
        return 1 if cur_sum == m else 0
    
    # 현재 원소를 포함하거나 포함하지 않는 경우
    return btc(cur_sum + arr[index], index + 1) + btc(cur_sum, index + 1)

result = btc(0, 0)
print(result - (1 if m == 0 else 0))
