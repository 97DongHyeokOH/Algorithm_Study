import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# dp[i] -> i번째 칸까지 가는 최소 점프 횟수, sys.maxsize인 경우에는 갈 수 없는곳
dp = [sys.maxsize]*n
dp[0] = 0

# 현재 칸까지 점프한 횟수에서 다음 칸으로 갈 수있는곳에 1을 더해서 최소값을 dp배열에 저장
for i in range(n):
    cur = dp[i]
    for j in range(1, arr[i]+1):
        if(i+j >= n):
            break

        if(cur+1 < dp[i+j]):
            dp[i+j] = cur+1

if(dp[n-1] == sys.maxsize):
    print(-1)
else:
    print(dp[n-1])
