import sys

def possible(a,b):
    if(0 <= a <= 1 and 0 <= b < n):
        return True
    return False

def value(y,x):
    val = arr[y][x]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for idx in range(4):
        a = dy[idx] + y
        b = dx[idx] + x

        if(possible(a,b)):
            val -= arr[a][b]
    
    return val

t = int(input())

for _ in range(t):
    n = int(input())

    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [list(0 for i in range(n)) for j in range(3)]
    
    for idx in range(n):
        if(idx == 0):
            dp[0][idx] = arr[0][idx]
            dp[1][idx] = arr[1][idx]
        else:
            dp[0][idx] = max(dp[1][idx-1], dp[2][idx-1]) + arr[0][idx]
            dp[1][idx] = max(dp[0][idx-1], dp[2][idx-1]) + arr[1][idx]

        if(idx+1 < n):
            dp[2][idx+1] = max(dp[0][idx], dp[1][idx])
    
    print(max(dp[0][n-1], dp[1][n-1]))