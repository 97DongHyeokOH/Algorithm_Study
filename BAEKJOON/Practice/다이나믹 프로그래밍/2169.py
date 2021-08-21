import sys

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# dp[i][j][k] -> i행 j열의 최대값을 저장하는 리스트 k가 0이면 왼쪽에서 온 경우의 최대값, k가 1이면 오른쪽에서 온 경우를 의미한다.
dp = [[[-INF, -INF] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        # 첫번째 행은 오른쪽으로만 갈 수 있다.
        if(i == 0):
            dp[i][j][0] = sum(arr[i][:j+1])
            continue

        if(j):
            dp[i][j][0] = max(dp[i][j-1][0] + arr[i][j],
                              max(dp[i-1][j]) + arr[i][j])
            dp[i][m-j-1][1] = max(dp[i][m-j][1] + arr[i]
                                  [m-j-1], max(dp[i-1][m-j-1]) + arr[i][m-j-1])
        else:
            dp[i][j][0] = max(dp[i-1][j]) + arr[i][j]
            dp[i][m-j-1][1] = max(dp[i-1][m-j-1]) + arr[i][m-j-1]

print(max(dp[n-1][m-1]))
