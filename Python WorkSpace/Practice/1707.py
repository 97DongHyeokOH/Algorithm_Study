import sys


def dfs(y, x):
    global result

    stack = [(y, x)]

    while(stack):
        a, b = stack.pop()

        if(color[a] and color[b]):
            if(color[a] == color[b]):
                result = False
                return
            else:
                continue

        if(color[a] == 0 and color[b] == 0):
            color[a] = 1
            color[b] = 2
        elif(color[a] == 0):
            color[a] = color[b] % 2 + 1
        elif(color[b] == 0):
            color[b] = color[a] % 2 + 1

        for i in arr[b]:
            stack.append((b, i))


t = int(sys.stdin.readline())

for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())

    color = [0]*v
    arr = [[] for _ in range(v)]
    result = True

    for i in range(e):
        n, m = map(int, sys.stdin.readline().split())
        arr[n-1].append(m-1)
        arr[m-1].append(n-1)

    for i in range(v):
        for j in arr[i]:
            if(not color[i] or not color[j]):
                dfs(i, j)
        if(not result):
            break

    if(result):
        print('YES')
    else:
        print('NO')
