import sys

input = sys.stdin.readline

n = int(input())

works = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*n
ans = 0

for i in range(n):
    t, p = works[i]
    
    if i + t - 1 < n:
        dp[i+t-1] = max(dp[i+t-1], ans+p)
    
    ans = max(ans, dp[i])

print(ans)