# 단순 도착지 까지 최단거리를 구하는 문제임
# BFS로 가장 먼저 도착한 길이 있으면 return 해주고
# BFS가 끝날 때 까지 도착점에 도착하지 않으면 -1 return

from collections import deque as dq


def solution(maps):
    n, m = len(maps), len(maps[0])
    visit = [[False]*m for _ in range(n)]

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    def pos(y, x):
        if(0 <= y < n and 0 <= x < m and maps[y][x]):
            return True
        return False

    q = dq([(0, 0, 1)])
    visit[0][0] = True

    while(q):
        y, x, cnt = q.popleft()

        if(y == n-1 and x == m-1):
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(pos(ny, nx) and not visit[ny][nx]):
                q.append((ny, nx, cnt+1))
                visit[ny][nx] = True

    return -1
