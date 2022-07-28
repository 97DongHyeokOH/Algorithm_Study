import sys

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[float("inf")]*3 for _ in range(n)]

for i in range(n):
    for j in range(3):
        if not i:
            dp[i][j] = cost[i][j]
        else:
            dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j-1)%3]) + cost[i][j]

print(min(dp[n-1]))