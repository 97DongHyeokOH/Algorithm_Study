import sys

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [0] * len(arr)
    k = 0

    for idx in range(len(arr)):
        k = max(k, arr[-idx-1])
        dp[-idx-1] = k
    
    result = 0

    for idx in range(len(arr)):
        result += (dp[idx] - arr[idx])
    
    print(result)