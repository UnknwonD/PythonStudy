n = int(input())

stack = []
for _ in range(n):
    command = input().split()
    
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if not stack else 0)
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)