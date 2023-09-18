import sys

input = sys.stdin.readline

# 배열을 벗어나는지 판단
def pos(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False

n, m, y, x, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

move = list(map(int, input().split()))

cur = [0, 0, 0, 0, 0, 0]

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

# 주사위 위치에 쓰여져있는 수를 cur에 저장하고, 주사위가 움직일 경우 cur안에서 수들을 변경
# cur = [윗면, 정면, 오른쪽, 뒷면, 왼쪽, 아랫면]
for d in move:
    ny = y + dy[d]
    nx = x + dx[d]
    
    if not pos(ny ,nx):
        continue
    
    if d == 1:
        cur = [cur[4], cur[1], cur[0], cur[3], cur[5], cur[2]]
    elif d == 2:
        cur = [cur[2], cur[1], cur[5], cur[3], cur[0], cur[4]]
    elif d == 3:
        cur = [cur[1], cur[5], cur[2], cur[0], cur[4], cur[3]]
    else:
        cur = [cur[3], cur[0], cur[2], cur[5], cur[4], cur[1]]
        
    if arr[ny][nx]:
        cur[5] = arr[ny][nx]
        arr[ny][nx] = 0
    else:
        arr[ny][nx] = cur[5]
        
    y, x = ny, nx
    
    print(cur[0])