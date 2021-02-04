import sys
from collections import deque as dq


def pos(y, x):
    if(0 <= y < n and 0 <= x < n):
        return True
    return False


def bfs(y, x):
    q = dq([(y, x)])
    visit[y][x] = True
    union = [(y, x)]

    while(q):
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(pos(ny, nx) and not visit[ny][nx] and l <= abs(arr[y][x] - arr[ny][nx]) <= r):
                union.append((ny, nx))
                q.append((ny, nx))
                visit[ny][nx] = True

    if(len(union) == 1):
        return 0

    num = 0

    for y, x in union:
        num += arr[y][x]

    num = int(num / len(union))

    for y, x in union:
        arr[y][x] = num

    return 1


n, l, r = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

result = 0

while(1):
    cnt = 0
    visit = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if(not visit[i][j]):
                cnt += bfs(i, j)

    print(arr)

    if(cnt):
        result += 1
    else:
        break

print(result)
