import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0]*n for _ in range(n)]

    for i in range(1,n):
        for y in range(n-i):
            x = y + i
            dp[y][x] = math.inf

            for j in range(y,x):
                dp[y][x] = min(dp[y][x], dp[y][j] + dp[j+1][x])
            dp[y][x] += sum(arr[y:x+1])
    
    print(dp[0][n-1])