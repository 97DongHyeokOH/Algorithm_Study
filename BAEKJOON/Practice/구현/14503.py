import sys

input = sys.stdin.readline


def pos(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False


n, m = map(int, input().split())

cur_y, cur_x, d = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(n)]

clear = [[False]*m for _ in range(n)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while(1):
    if not clear[cur_y][cur_x]:
        clear[cur_y][cur_x] = True
        cnt += 1

    can_move = False

    for i in range(4):
        ny = cur_y + dy[(d-i-1) % 4]
        nx = cur_x + dx[(d-i-1) % 4]

        if pos(ny, nx) and not clear[ny][nx] and area[ny][nx] == 0:
            can_move = True
            cur_y, cur_x = ny, nx
            d = (d-i-1) % 4
            break

    if not can_move:
        ny = cur_y + dy[(d+2) % 4]
        nx = cur_x + dx[(d+2) % 4]

        if not pos(ny, nx) or area[ny][nx] == 1:
            break

        cur_y, cur_x = ny, nx

print(cnt)
