import sys
import copy

input = sys.stdin.readline


def pos(y, x):
    if(0 <= y < 12 and 0 <= x < 6):
        return True
    return False


puyo = [list(input().rstrip()) for _ in range(12)]

result = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

boom = True

while(boom):
    visit = [[False]*6 for _ in range(12)]
    boom = False

    for y in range(12):
        for x in range(6):
            if(puyo[y][x] != '.' and not visit[y][x]):
                queue = [(y, x)]
                blocks = [(y, x)]
                visit[y][x] = True

                while(queue):
                    y, x = queue.pop(0)

                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]

                        if(pos(ny, nx) and not visit[ny][nx] and puyo[ny][nx] == puyo[y][x]):
                            visit[ny][nx] = True
                            blocks.append((ny, nx))
                            queue.append((ny, nx))

                if(len(blocks) >= 4):
                    boom = True

                    for ty, tx in blocks:
                        puyo[ty][tx] = '.'

    if(boom):
        result += 1

    next_puyo = [['.']*6 for _ in range(12)]

    for x in range(6):
        ny = 11
        for y in range(11, -1, -1):
            if(puyo[y][x] != '.'):
                next_puyo[ny][x] = puyo[y][x]
                ny -= 1

    puyo = copy.deepcopy(next_puyo)

print(result)
