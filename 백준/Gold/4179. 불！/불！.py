import sys
from collections import deque

input = sys.stdin.readline

# 해당 위지로 지훈이가 이동 가능한 경우
def pos(y, x):
    if 0 <= y < r and 0 <= x < c and maze[y][x] == '.':
        return True
    return False

# 다음에 지훈이가 탈출 할 수 있는 경우
def can_escape(y, x):
    if y == 0 or y == r-1 or x == 0 or x == c-1:
        return True
    return False

r, c = map(int, input().split())

maze = [list(input().rstrip()) for _ in range(r)]

j_pos = deque([])
f_pos = deque([])
j_visit = [[False]*c for _ in range(r)]
f_visit = [[False]*c for _ in range(r)]
cur_time = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for y in range(r):
    for x in range(c):
        if maze[y][x] == 'J':
            j_pos.append((0, y, x))
            j_visit[y][x] = True
        elif maze[y][x] == 'F':
            f_pos.append((y, x))
            f_visit[y][x] = True
                
while j_pos:
    next_fire = []
    
    for fy, fx in f_pos:
        for i in range(4):
            ny = fy + dy[i]
            nx = fx + dx[i]
            
            if pos(ny, nx) and not f_visit[ny][nx]:
                next_fire.append((ny,nx))
                f_visit[ny][nx] = True
                
    f_pos = next_fire
    
    while j_pos:
        t, jy, jx = j_pos.popleft()
        
        if t > cur_time:
            j_pos.append((t, jy, jx))
            break
        
        # 가장자리에 위치해 있다면 1초 뒤 탈출 가능
        if can_escape(jy, jx):
            print(t+1)
            exit(0)
        
        for i in range(4):
            ny = jy + dy[i]
            nx = jx + dx[i]
            
            # 다음 위치로 지훈이가 이동 가능하고, 해당 지역에 불이 붙는 시간보다 지훈이의 시간이 작은 경우
            if pos(ny, nx) and not j_visit[ny][nx] and not f_visit[ny][nx]:
                j_pos.append((t+1, ny, nx))
                j_visit[ny][nx] = True
                
    cur_time += 1
            
print('IMPOSSIBLE')