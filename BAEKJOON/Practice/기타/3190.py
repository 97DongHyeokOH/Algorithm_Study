import sys
from collections import deque

input = sys.stdin.readline

# 리스트를 벗어나는지 판단


def pos(y, x):
    if(0 <= y < n and 0 <= x < n):
        return True
    return False


n = int(input())

k = int(input())

# 사과가 있는 자리는 1을 넣어준다.
apple = [[0]*n for _ in range(n)]

for _ in range(k):
    y, x = map(int, input().split())
    apple[y-1][x-1] = 1

l = int(input())

# change 리스트에 있는 (a,b) -> a초 뒤에 b로 방향이 틀어진다.
change = [list(input().rstrip().split()) for _ in range(l)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
# 뱀이 있는 좌표를 저장한 queue(deque)
# 앞의 인덱스가 머리쪽 뒤로 갈수록 꼬리쪽
snake = deque([])
result = 0
move = 0

snake.append((0, 0))
idx = 0

# 벽에 부딪치거나 뱀이 있는 위치로 움직일때까지 움직인다
while(1):
    y, x, = snake[0]

    result += 1

    ny, nx = y + dy[move], x + dx[move]

    if(not pos(ny, nx) or (ny, nx) in set(snake)):
        print(result)
        break

    snake.appendleft((ny, nx))

    # 사과가 있으면 길이가 늘어나고 사과가 없어진다.
    if(apple[ny][nx] == 0):
        snake.pop()
    else:
        apple[ny][nx] = 0

    # result초 뒤에 방향을 변경
    try:
        if(result == int(change[idx][0])):
            if(change[idx][1] == 'D'):
                move = (move + 1) % 4
            else:
                move = (move - 1) % 4
            idx += 1
    except IndexError:
        continue
