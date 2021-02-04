import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
dp = []

for i in arr:
    idx = len(dp)-1

    if(idx == -1 or dp[idx] < i):
        dp.append(i)
    else:
        while(idx > -1):
            if(idx == 0 and dp[idx] > i):
                dp[idx] = i
            elif(dp[idx] < i):
                dp[idx+1] = i
                break
            idx -= 1

print(len(dp))