import sys

n, m, h = map(int, sys.stdin.readline().split())
# dp[i] -> 높이가 i인 탑을 만들 수 있는 경우의 수
dp = [0]*(h+1)
dp[0] = 1

for _ in range(n):
    blocks = list(map(int, sys.stdin.readline().split()))
    temp = dp.copy()

    for i in range(h+1):
        # 높이가 i인 탑을 만들 수 있을 때, 다른 블록들을 쌓아준다.
        if(dp[i]):
            for block in blocks:
                # 현재 탑에서 block을 쌓으면 h보다 작거나 같은 높이의 탑이 만들어 질 때
                if(i + block <= h):
                    temp[i+block] += dp[i]

    dp = temp.copy()

print(dp[h] % 10007)
