import sys

n, m = map(int, sys.stdin.readline().split())
app = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
k = sum(cost)+1
dp = [0]*(k)

for i in range(n):
    temp = dp.copy()
    c = cost[i]
    a = app[i]
    for j in range(k-c):
        if(temp[j]):
            dp[j+c] = max(dp[j+c], temp[j]+a)
    dp[c] = max(dp[c], a)

for i in range(k):
    if(dp[i] >= m):
        print(i)
        exit(0)

print(-1)
