n = int(input())

dp = [0]*(n+1)

result = 0

for idx in range(0, n):
    t,p = map(int, input().split())

    dp[idx] = max(result, dp[idx])

    if(idx + t <= n):
        dp[idx + t] = max(dp[idx + t], dp[idx] + p)
    
    result = max(result, dp[idx])

result = max(result, dp[n])

print(result)