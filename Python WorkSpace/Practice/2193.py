n = int(input())

dp = [1, 1]

for idx in range(2, n):
    dp.append(dp[idx-1] + dp[idx-2])

print(dp.pop())