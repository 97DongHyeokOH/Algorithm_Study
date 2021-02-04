import sys
from collections import deque as dq


# def goal_in(y, x, direc):  # direct -> 0: down 1: up 2: right 3: left
def move(y, x, dy, dx):
    cnt = 0

    while(arr[y+dy][x+dx] != '#' and arr[y][x] != 'O'):
        x += dx
        y += dy
        cnt += 1

    return y, x, cnt


def solution():

    while(q):
        ry, rx, by, bx, cnt = q.popleft()

        if(cnt >= 10):
            break

        for i in range(4):
            n_ry, n_rx, r_cnt = move(ry, rx, dy[i], dx[i])
            n_by, n_bx, b_cnt = move(by, bx, dy[i], dx[i])

            if(arr[n_by][n_bx] == 'O'):
                continue

            if(arr[n_ry][n_rx] == 'O'):
                return cnt+1

            if(n_ry == n_by and n_rx == n_bx):
                if(r_cnt < b_cnt):
                    n_by -= dy[i]
                    n_bx -= dx[i]
                else:
                    n_ry -= dy[i]
                    n_rx -= dx[i]

            if(not visit[n_ry][n_rx][n_by][n_bx]):
                visit[n_ry][n_rx][n_by][n_bx] = True
                q.append((n_ry, n_rx, n_by, n_bx, cnt+1))

    return -1


n, m = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for j in range(m):
    for i in range(n):
        if(arr[i][j] == 'R'):
            ry, rx = i, j
        elif(arr[i][j] == 'B'):
            by, bx = i, j

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q = dq([(ry, rx, by, bx, 0)])

print(solution())
