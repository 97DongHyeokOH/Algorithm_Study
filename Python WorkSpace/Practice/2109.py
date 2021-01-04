import sys

n = int(input())

arr = []
max_day = 0

for _ in range(n):
    p,d = map(int, sys.stdin.readline().split())

    max_day = max(max_day, d)

    arr.append((d,p))

dp = [0] * (max_day + 1)

arr.sort(key=lambda x: (-x[1], x[0]))

for i in arr:
    idx = i[0]
    money = i[1]

    while(idx):
        if(dp[idx] < money):
            dp[idx] = money
            break
        idx -= 1

print(sum(dp))