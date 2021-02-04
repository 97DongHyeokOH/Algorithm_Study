import sys
from collections import deque as dq


def pos(y, x):
    if(0 <= y < n and 0 <= x < n):
        return True
    return False


def bfs1():  # 일반인
    q = dq([])
    visit = [[False]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if(not visit[i][j]):
                temp = color[i][j]
                q.append((i, j))
                visit[i][j] = True

                while(q):
                    y, x = q.popleft()

                    for idx in range(4):
                        ny = y + dy[idx]
                        nx = x + dx[idx]

                        if(pos(ny, nx) and temp == color[ny][nx] and not visit[ny][nx]):
                            q.append((ny, nx))
                            visit[ny][nx] = True
                cnt += 1
    return cnt


def bfs2():  # 적록색약
    q = dq([])
    visit = [[False]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if(color[i][j] == 'G'):
                color[i][j] = 'R'

    for i in range(n):
        for j in range(n):
            if(not visit[i][j]):
                temp = color[i][j]
                q.append((i, j))
                visit[i][j] = True

                while(q):
                    y, x = q.popleft()

                    for idx in range(4):
                        ny = y + dy[idx]
                        nx = x + dx[idx]

                        if(pos(ny, nx) and temp == color[ny][nx] and not visit[ny][nx]):
                            q.append((ny, nx))
                            visit[ny][nx] = True
                cnt += 1
    return cnt


n = int(sys.stdin.readline())

color = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

print(bfs1(), bfs2())
