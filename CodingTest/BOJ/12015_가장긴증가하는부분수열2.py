from bisect import bisect_left

N = int(input())
data = list(map(int, input().split()))

stack = []

for i in range(N):
    if len(stack) == 0 or stack[-1] < data[i]:
        stack.append(data[i])
    else:
        idx = bisect_left(stack, data[i])
        stack[idx] = data[i]

print(len(stack))
print(' '.join(stack))