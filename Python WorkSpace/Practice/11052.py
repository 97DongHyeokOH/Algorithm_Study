n = int(input())

arr = list(map(int, input().split()))
dp = [0]*(n+1)

for idx in range(n):
    dp[idx+1] = arr[idx]

    for i in range(1, (idx+1)//2 + 1):
        dp[idx+1] = max(dp[idx+1], dp[i] + dp[idx+1-i])

print(dp[idx+1])