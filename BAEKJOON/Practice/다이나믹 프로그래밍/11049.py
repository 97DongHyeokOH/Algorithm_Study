import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        t = i + j
        dp[j][t] = sys.maxsize

        for k in range(j, t):
            dp[j][t] = min(dp[j][t], dp[j][k] + dp[k+1][t] +
                           matrix[j][0]*matrix[k][1]*matrix[t][1])

print(dp[0][n-1])
