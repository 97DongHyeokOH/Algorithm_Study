import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())

change_vol = list(map(int, input().split()))

# dp[i][j] -> i 번째 곡을 연주하기 전에 j 볼륨에 접근 할 수있는가를 판단하는 dp배열 -> 1이라면 해당 볼륨을 맞출수 있고, 0이면 불가능하다.
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if(not dp[i][j]):
            continue

        vol = change_vol[i]

        if(j - vol >= 0):
            dp[i+1][j - vol] = 1
        if(j + vol <= m):
            dp[i+1][j + vol] = 1

idx = m

while(idx > -1):
    if(dp[n][idx]):
        print(idx)
        exit(0)
    idx -= 1

print(-1)