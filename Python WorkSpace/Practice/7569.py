import sys
from collections import deque as dq

def pos(z,y,x):
    if(0 <= y < m and 0 <= x < n and 0 <= z < h and tomato[z][y][x] == 0):
        return True
    return False

def bfs():
    queue = dq([])
    result = 0

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if(tomato[i][j][k] == 1):
                    queue.append((i,j,k,0))
    
    while(queue):
        z,y,x,day = queue.popleft()

        result = max(result, day)

        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            nz = z + dz[i]

            if(pos(nz,ny,nx)):
                tomato[nz][ny][nx] = 1
                queue.append((nz,ny,nx,day+1))
    
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if(tomato[z][y][x] == 0):
                    return -1
    
    return result

n,m,h = map(int, sys.stdin.readline().split())

dy = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

tomato = [[list(map(int, sys.stdin.readline().split())) for k in range(m)] for l in range(h)]

print(bfs())