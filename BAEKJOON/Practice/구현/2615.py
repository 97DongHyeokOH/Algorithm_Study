import sys

input = sys.stdin.readline


def pos(y, x):
    if 0 <= y < 19 and 0 <= x < 19:
        return True
    return False


omok = [list(map(int, input().split())) for _ in range(19)]
visit = [[[False]*4 for _ in range(19)] for _ in range(19)]

result = 0

dy = [0, 1, 1, 1]
dx = [1, 0, 1, -1]

for y in range(19):
    for x in range(19):
        if omok[y][x] and not result:
            for i in range(4):
                if visit[y][x][i]:
                    continue

                cnt = 1
                ny, nx = y, x

                while(1):
                    ny += dy[i]
                    nx += dx[i]

                    if pos(ny, nx) and omok[ny][nx] == omok[y][x]:
                        cnt += 1
                        visit[ny][nx][i] = True
                    else:
                        break

                if cnt == 5 and i < 3:
                    result = omok[y][x]
                    ry, rx = y+1, x+1
                elif cnt == 5 and i == 3:
                    result = omok[y][x]
                    ry, rx = y+5, x-3

                visit[y][x][i] = True

print(result)

if result:
    print(ry, rx)
