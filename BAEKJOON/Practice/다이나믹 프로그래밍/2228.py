# 문제: N(1≤N≤100)개의 수로 이루어진 1차원 배열이 있다. 이 배열에서 M(1≤M≤⌈(N/2)⌉)개의 구간을 선택해서, 구간에 속한 수들의 총 합이 최대가 되도록 하려 한다. 단, 다음의 조건들이 만족되어야 한다.
# 각 구간은 한 개 이상의 연속된 수들로 이루어진다.
# 서로 다른 두 구간끼리 겹쳐있거나 인접해 있어서는 안 된다.
# 정확히 M개의 구간이 있어야 한다. M개 미만이어서는 안 된다.
# N개의 수들이 주어졌을 때, 답을 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 배열을 이루는 수들이 차례로 주어진다. 배열을 이루는 수들은 -32768 이상 32767 이하의 정수이다.

# 출력: 첫째 줄에 답을 출력한다.

import sys

n, m = map(int, sys.stdin.readline().split())

# 배열을 입력받아 list에 저장
arr = [int(sys.stdin.readline()) for _ in range(n)]
# i번째 수까지의 합을 저장해줌 (연속된 숫자들의 합을 구하기 위함)
sum = [0]
# sum에 값을 저장하기 위한 임의변수
temp = 0

# sum list를 채워 줌
for i in arr:
    temp += i
    sum.append(temp)

# dp[i][j] i개의 배열로 j개의 구간을 선택했을 때 최대 값
dp = [[0] + [-sys.maxsize]*(m) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j]
        for k in range(1, i+1):
            if(k >= 2):
                dp[i][j] = max(dp[i][j], dp[k-2][j-1] + sum[i] - sum[k-1])
            elif(k == 1 and j == 1):
                dp[i][j] = max(dp[i][j], sum[i])

# m개의 구간을 가진상태에서의 최대 합
print(dp[n][m])
