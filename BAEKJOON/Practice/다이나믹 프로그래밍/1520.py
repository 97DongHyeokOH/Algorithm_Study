import sys

sys.setrecursionlimit(100000)

def possible(a,b):
    if(0 <= a < n and 0 <= b < m):
        return True
    return False

def dfs(y,x):
    if(y == n-1 and x == m-1):
        return 1
    
    if(dp[y][x] != -1):
        return dp[y][x]
    
    dp[y][x] = 0
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if(possible(ny,nx) and arr[y][x] > arr[ny][nx]):
            dp[y][x] += dfs(ny,nx)
    
    return dp[y][x]

n,m = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]

print(dfs(0,0))