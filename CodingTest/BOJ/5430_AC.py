import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    funcs = input().strip()
    n = int(input())
    arr_raw = input().strip()

    # 입력 처리
    if arr_raw == '[]':
        arr = deque()
    else:
        arr = deque(map(int, arr_raw[1:-1].split(',')))

    reverse = False
    error = False

    for cmd in funcs:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if not arr:
                error = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if error:
        print('error')
    else:
        if reverse:
            arr.reverse()
        print(f"[{','.join(map(str, arr))}]")
