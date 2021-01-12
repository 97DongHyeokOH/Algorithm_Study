import sys

def possible(a,b):
    if(0 <= a < n and 0 <= b < n):
        return True
    return False

def dfs(y,x):
    if(y == n-1 and x == n-1):
        return 1
    if(dp[y][x] != -1):
        return dp[y][x]
    
    dp[y][x] = 0
    k = arr[y][x]
    
    dy = [k, 0]
    dx = [0, k]

    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]

        if(possible(ny,nx)):
            dp[y][x] += dfs(ny,nx)
    
    return dp[y][x]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

print(dfs(0,0))