import sys

input = sys.stdin.readline


def pos(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False


def solution():
    temp_array = [[0]*m for _ in range(n)]
    visit = [[False]*m for _ in range(n)]

    for i in range(n):
        temp_array[i] = array[i][:]

    for i in range(min(n, m)//2):
        cy, cx = i, i

        for idx in range(4):

            while(1):
                ny = cy + dy[idx]
                nx = cx + dx[idx]

                if not pos(ny, nx) or visit[ny][nx]:
                    break

                array[ny][nx] = temp_array[cy][cx]
                visit[ny][nx] = True
                cy, cx = ny, nx


n, m, r = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for _ in range(r):
    solution()

for i in range(n):
    print(*array[i])
