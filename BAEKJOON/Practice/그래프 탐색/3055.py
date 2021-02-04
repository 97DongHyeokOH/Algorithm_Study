import sys
from collections import deque as dq


def pos(y, x):
    if(0 <= y < r and 0 <= x < c and not water[y][x] and not stone[y][x]):
        return True
    return False


def bfs():
    global water_temp
    global beaver_temp

    while(beaver_temp):
        w_q = dq(water_temp)
        water_temp = []

        while(w_q):
            wy, wx = w_q.popleft()

            for i in range(4):
                n_wy = wy + dy[i]
                n_wx = wx + dx[i]

                if(pos(n_wy, n_wx) and arr[n_wy][n_wx] != 'D'):
                    water[n_wy][n_wx] = True
                    water_temp.append((n_wy, n_wx))

        b_q = dq(beaver_temp)
        beaver_temp = []
        while(b_q):
            by, bx, cnt = b_q.popleft()
            if((by, bx) == hole):
                return cnt

            for i in range(4):
                n_by = by + dy[i]
                n_bx = bx + dx[i]

                if(pos(n_by, n_bx) and not beaver[n_by][n_bx]):
                    beaver[n_by][n_bx] = True
                    beaver_temp.append((n_by, n_bx, cnt+1))

    return -1


r, c = map(int, sys.stdin.readline().split())

arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]
water = [[False]*c for _ in range(r)]
beaver = [[False]*c for _ in range(r)]
stone = [[False]*c for _ in range(r)]
w_q = dq([])
b_q = dq([])
water_temp = []
beaver_temp = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if(arr[i][j] == '*'):
            water[i][j] = True
            water_temp.append((i, j))
        elif(arr[i][j] == 'S'):
            beaver[i][j] = True
            beaver_temp.append((i, j, 0))
        elif(arr[i][j] == 'D'):
            hole = (i, j)
        elif(arr[i][j] == 'X'):
            stone[i][j] = True

result = bfs()

if(result == -1):
    print('KAKTUS')
else:
    print(result)
