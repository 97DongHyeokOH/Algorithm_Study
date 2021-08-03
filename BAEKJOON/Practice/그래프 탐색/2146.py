import sys

/


def pos(y, x):
    if(0 <= y < n and 0 <= x < n):
        return True
    return False


def solution(y, x):
    sub_visit = [[False]*n for _ in range(n)]
    sub_visit[y][x] = True
    this_land = [[y, x]]
    queue = []

    while(this_land):
        ay, ax = this_land.pop(0)

        for i in range(4):
            ny = ay + dy[i]
            nx = ax + dx[i]

            if(pos(ny, nx) and not sub_visit[ny][nx]):
                if(land[ny][nx]):
                    this_land.append([ny, nx])
                    sub_visit[ny][nx] = True
                    visit[ny][nx] = True
                else:
                    queue.append([1, ny, nx])
                    sub_visit[ny][nx] = True

    while(queue):
        cnt, ay, ax = queue.pop(0)

        for i in range(4):
            ny = ay + dy[i]
            nx = ax + dx[i]

            if(pos(ny, nx) and not sub_visit[ny][nx]):
                if(land[ny][nx]):
                    result.append(cnt)
                    return
                else:
                    queue.append([cnt+1, ny, nx])
                    sub_visit[ny][nx] = True


n = int(sys.stdin.readline())

land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
result = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if(land[i][j] and not visit[i][j]):
            visit[i][j] = True
            solution(i, j)

print(min(result))
