import sys

num = sys.stdin.readline().replace('\n', '')

zero = one = 0 # 0으로 바꾸거나 1로 바꾸는 경우의 수 확인


for i in range(len(num)):
    if num[i-1] != num[i]:
        if num[i-1] == '0':
            one += 1
        elif num[i-1] == '1':
            zero += 1

print(min(zero, one))