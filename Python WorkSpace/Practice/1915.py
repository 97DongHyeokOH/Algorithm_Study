import sys

sys.setrecursionlimit(100000)

def pos(y,x):
    if(y < n and x < m):
        return True
    return False

def square(y,x):
    temp = []

    if(dp[y][x]):
        return dp[y][x]

    if(arr[y][x] == '1'):
        dp[y][x] = 1
    else:
        return 0

    for i in range(3):
        ny = y + dy[i]
        nx = x + dx[i]

        if(pos(ny,nx) and arr[ny][nx] == '1'):
            temp.append(square(ny,nx))
        else:
            return 1
    
    dp[y][x] += min(temp)
    
    return dp[y][x]


n,m = map(int, sys.stdin.readline().split())

arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
result = 0

dy = [1, 0, 1]
dx = [0, 1, 1]

for y in range(n):
    for x in range(m):
        result = max(result, square(y,x))

print(result**2)