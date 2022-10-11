import sys

input = sys.stdin.readline

t, w = map(int, input().split())

arr = [int(input()) for _ in range(t)]
# dp[i][j] -> i번 움직이고, 현재 시간이 j일 때, 받은 최대 자두 수
dp = [[0]*(t+1) for _ in range(w+2)]
# 결과 값
result = 0

for i in range(w+1):
    for j in range(t):
        # 만약 i가 0 또는 짝수라면 현재 1번 나무 밑에 위치한다
        if (i+1) % 2 == arr[j] % 2:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + 1)
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
        # 만약 i가 홀수라면 현재 2번 나무 밑에 위치한다.
        else:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
        
        # 마지막 자두까지 다 떨어지면 i번 움직인 경우 받을 수 있는 최대 값을 결과 값에 최신화 한다.
        if j == t-1:
            result = max(result, dp[i][j+1])

print(result)