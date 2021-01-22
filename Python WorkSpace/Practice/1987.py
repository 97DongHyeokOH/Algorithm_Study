# pypy3으로 채점

import sys

def pos(y,x):
    if(0 <= y < r and 0 <= x < c):
        idx = ord(arr[y][x]) - 65
        if(not alpha[idx]):
            return True
    return False

def no_way(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if(pos(ny,nx)):
            return False
    return True

def dfs(y,x,n):
    global result

    idx = ord(arr[y][x]) - 65

    alpha[idx] = 1
    result = max(result, n)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if(pos(ny,nx)):
            k = ord(arr[ny][nx]) - 65
            dfs(ny,nx,n+1)
            alpha[k] = 0

    return

r,c = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
alpha = [0]*26
stack = []
result = 0

dy = [1,-1,0,0]
dx = [0,0,1,-1]

dfs(0,0,1)

print(result)