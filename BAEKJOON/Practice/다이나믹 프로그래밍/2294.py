import sys

n,k = map(int, sys.stdin.readline().split())
arr = []
dp = [100000]*(k+1)
cnt = 0

for _ in range(n):
    coin = int(sys.stdin.readline())
    arr.append(coin)

arr.sort(reverse=True)

for coin in arr:
    for idx in range(coin, k+1):
        if(idx % coin == 0):
            dp[idx] = min(idx // coin, dp[idx])
        
        if(0 < dp[idx-coin]):
            dp[idx] = min(dp[idx-coin] + 1, dp[idx])
    
if(dp[k] == 100000):
    print(-1)
else:
    print(dp[k])