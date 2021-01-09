n = int(input())

arr = list(map(int, input().split()))
dp = [1]*n

for idx in range(n):
    for j in range(idx+1):
        if(arr[idx] < arr[j]):
            dp[idx] = max(dp[idx], dp[j]+1)

print(max(dp))