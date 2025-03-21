N = input()
mid = len(N)//2
left = list(map(int, list(N[:mid])))
right = list(map(int, list(N[mid:])))

if sum(left) == sum(right):
    print('LUCKY')
else:
    print("READY")