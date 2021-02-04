n = int(input())

arr = list(map(int, input().split()))
dp = [0]*n

for idx in range(n):
    temp = 0
    for j in range(idx+1):
        if(arr[j] < arr[idx]):
            temp = max(temp, dp[j])
    dp[idx] = temp + arr[idx]

print(max(dp))