import sys
from collections import deque as dq


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


def bfs(a, b):
    q = dq([(a, b, 0)])
    temp_visit = [[False]*m for _ in range(n)]
    temp_visit[a][b] = True

    while(q):
        y, x, cnt = q.popleft()

        node = Node((y, x))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            n_node = Node((ny, nx))

            if(pos(ny, nx) and not temp_visit[ny][nx]):
                q.append((ny, nx, cnt+1))
                temp_visit[ny][nx] = True
                n_node.prev = node

    while(node.prev):
        y, x = node.data
        visit[y][x] = True
        node = node.prev

    return cnt


def pos(y, x):
    if(0 <= y < n and 0 <= x < m and arr[y][x] == 'L'):
        return True
    return False


n, m = map(int, sys.stdin.readline().split())

arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
ans = 0

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if(not visit[i][j] and arr[i][j] == 'L'):
            ans = max(ans, bfs(i, j))

print(ans)
