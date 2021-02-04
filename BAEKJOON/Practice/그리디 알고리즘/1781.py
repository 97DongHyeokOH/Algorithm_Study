import sys

n = int(input())

dp = [0] * (n+1)
arr = []

for _ in range(n):
    d, s = map(int, sys.stdin.readline().split())
    arr.append((d, s))

arr.sort(key=lambda x: (-x[1], x[0]))

for i in arr:
    idx = i[0]
    score = i[1]

    while(idx):
        if(not dp[idx]):
            dp[idx] = score
            break
        idx -= 1

print(sum(dp))