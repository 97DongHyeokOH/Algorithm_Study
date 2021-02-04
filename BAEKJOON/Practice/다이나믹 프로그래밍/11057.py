n = int(input())

dp = [0]*10
result = 0

for _ in range(n):
    for idx in range(10):
        if(idx == 0):
            dp[idx] = 1
        else:
            dp[idx] += dp[idx-1]
            dp[idx] %= 10007

print(sum(dp) % 10007)