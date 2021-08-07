import sys

n = int(sys.stdin.readline())
children = [int(sys.stdin.readline()) for _ in range(n)]
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if(children[j] < children[i]):
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
