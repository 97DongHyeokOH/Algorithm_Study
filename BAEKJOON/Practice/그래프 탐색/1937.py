import sys

sys.setrecursionlimit(100000)

def pos(y,x):
    if(0 <= y < n and 0 <= x < n):
        return True
    return False

def way(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if(pos(ny,nx) and arr[ny][nx] > arr[y][x]):
            return True

    return False

def dfs(y,x):
    if(not way(y,x)):
        return 1
    
    if(dp[y][x] != 1):
        return dp[y][x]
    
    for idx in range(4):
        ny = y + dy[idx]
        nx = x + dx[idx]

        if(pos(ny,nx) and arr[ny][nx] > arr[y][x]):
            dp[y][x] = max(dp[y][x], 1 + dfs(ny,nx))
        
    return dp[y][x]

n = int(sys.stdin.readline())

arr = []
dp = [[1]*n for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]
result = 0

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

for y in range(n):
    for x in range(n):
        result = max(result, dfs(y,x))

print(result)