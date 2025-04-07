def dfs(cur, oper, result):
    if sum(oper) == 0:
        ans.add(result)
        return
    
    for i, op in enumerate(oper):
        if op == 0:
            continue
        
        # 연산이 가능하면, 연산 추가해서 실행
        if i == 0: # 덧셈
            tmp = result + num[cur]
        elif i == 1: # 뺄셈
            tmp = result - num[cur]
        elif i == 2: # 곱셈
            tmp = result * num[cur]
        else: # 나눗셈
            if result < 0:
                tmp = -(-result // num[cur])
            else:
                tmp = result // num[cur]

        oper[i] -= 1
        dfs(cur+1, oper, tmp)
        oper[i] += 1

n = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))
ans = set()

dfs(1, operators, num[0])

print(max(ans))
print(min(ans))