import sys

input = sys.stdin.readline

# dp[i][j] -> j번 한 개짜리 알약을 꺼냈고, i번 반 개짜리 알약을 꺼냈다.
# 한 개의 알약을 꺼낸 횟수보다 반 개 알약을 많이 꺼낼 수는 없다.
# n개의 알약이 들어 있으면 결국 한 개를 n번 꺼내고, 반 개를 n번 꺼내야 한다. -> dp[n][n]
dp = [[0]*31 for _ in range(31)]

for i in range(31):
    for j in range(31):
        # 한 개의 알약을 꺼낸 횟수보다 반 개 알약을 많이 꺼낼 수는 없다.
        if i > j:
            continue
        
        # 반 개짜리 알약은 적어도 한 개짜리 알약을 1번 이상 꺼내야 한다.
        if i == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

while 1:
    n = int(input())
    
    if not n:
        break

    print(dp[n][n])