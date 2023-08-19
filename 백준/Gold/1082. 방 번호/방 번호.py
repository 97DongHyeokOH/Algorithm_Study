import sys

input = sys.stdin.readline
    
n = int(input())
price = list(map(int, input().split()))
coin = int(input())

dp = [0]*(coin+1)

for i in range(coin+1):
    if i and not dp[i]:
        continue
    
    for j, k in enumerate(price):
        if i + k > coin:
            continue
        
        dp[i+k] = max(dp[i+k], dp[i]*10 + j)

print(max(dp))