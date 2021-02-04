import sys
from collections import deque as dq

sys.setrecursionlimit(100000000)


def pos(y, x):
    if(0 <= y < n and 0 <= x < m):
        return True
    return False


def bfs():
    q = dq([(0, 0, 1, 1)])
    result = sys.maxsize

    while(q):
        y, x, k, crash = q.popleft()

        if(y == n-1 and x == m-1):
            result = min(result, k)
            continue

        if(visit[y][x][crash]):
            continue

        visit[y][x][crash] = True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(pos(ny, nx)):
                if(arr[ny][nx] == '0'):
                    q.append((ny, nx, k+1, crash))
                elif(arr[ny][nx] == '1' and crash):
                    q.append((ny, nx, k+1, 0))

    if(result == sys.maxsize):
        return -1

    return result


n, m = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visit = [[[False, False] for i in range(m)] for _ in range(n)]
result = sys.maxsize

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

print(bfs())
