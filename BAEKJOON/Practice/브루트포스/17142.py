import sys
from itertools import combinations
import heapq

input = sys.stdin.readline


def pos(y, x):
    if(0 <= y < n and 0 <= x < n and lab[y][x] != 1):
        return True
    return False


def bfs(temp):
    queue = []
    visit = [[False]*n for _ in range(n)]
    result = 0

    for y, x in temp:
        heapq.heappush(queue, (0, y, x))
        visit[y][x] = True

    while(queue):
        cnt, y, x = heapq.heappop(queue)
        if(lab[y][x] == 0):
            result = max(result, cnt)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(pos(ny, nx) and not visit[ny][nx]):
                heapq.heappush(queue, (cnt+1, ny, nx))
                visit[ny][nx] = True

    for i in range(n):
        for j in range(n):
            if(lab[i][j] == 0 and not visit[i][j]):
                result = sys.maxsize

    return result


n, m = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(n)]

virus = []
wall = []

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(n):
    for j in range(n):
        if(lab[i][j] == 2):
            virus.append((i, j))
        if(lab[i][j] == 1):
            wall.append((i, j))

temp = list(combinations(virus, m))
result = sys.maxsize

for t in temp:
    result = min(result, bfs(t))

if(result == sys.maxsize):
    print(-1)
else:
    print(result)
