import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
# dp[i][j] -> i개의 색중에 j개를 선택해 만들수 있는 경우의 수
dp = [[0] * (k+1) for _ in range(n+1)]

# dp배열 초기화
for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

# i번째 색을 선택할 경우에 i번째 색을 칠하는 경우 + i번째 색을 칠하지 않는 경우
# -> dp[i-2][j-1](포함되는 경우) + dp[i-1][j](포함되지 않는 경우)를 dp[i][j]에 넣어준다.
# 아래의 for문에서는 원형으로 되어있다는 것을 생각하지 않고 일직선상이라고 생각하고 값을 넣어준다.
for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % 1000000003

# 마지막인 경우에는 i번째가 포함되는 경우에 첫번째의 색도 포함되면 안되기 때문에 dp[i-3][j-1] + dp[i][j]값을 넣어준다.
answer = (dp[n-3][k-1] + dp[n-1][k]) % 1000000003
print(answer)
