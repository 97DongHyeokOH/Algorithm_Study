import sys

input = sys.stdin.readline


def pos(y, x):
    if 0 <= y < r and 0 <= x < c:
        return True
    return False


r, c, n = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(r)]
timer = [[0]*c for _ in range(r)]

bomb = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for y in range(r):
    for x in range(c):
        if arr[y][x] == 'O':
            timer[y][x] = 2

for i in range(1, n):
    for y in range(r):
        for x in range(c):
            if arr[y][x] == '.':
                arr[y][x] = 'O'
                timer[y][x] = 0

    for y in range(r):
        for x in range(c):
            if timer[y][x] == 3:
                arr[y][x] = '.'
                timer[y][x] = 0

                for idx in range(4):
                    ny = y + dy[idx]
                    nx = x + dx[idx]

                    if pos(ny, nx) and arr[ny][nx] == 'O' and timer[ny][nx] < 3:
                        arr[ny][nx] = '.'
                        timer[ny][nx] = 0

    for y in range(r):
        for x in range(c):
            if arr[y][x] == 'O':
                timer[y][x] += 1


for y in range(r):
    for x in range(c):
        print(arr[y][x], end='')
    print()
