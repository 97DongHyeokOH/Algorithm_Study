import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    # dp[i] -> 동전으로 금액이 i원인 금액을 만들 수 있는 경우의 수
    dp = [0]*(m+1)
    dp[0] = 1

    # 금액이 i로 만들수 있는 경우의 수는
    # 이전까지 코인들로 금액 i를 만든 경우의 수 + 현재 금액이 coin원인 코인을 이용해서 (i-coin)원을 만든 경우의 수
    for coin in coins:
        temp = [0]*(m+1)

        for i in range(m+1):
            # 현재 코인 보다 작은 경우는 이전 코인들로 만들 수 있는 경우의 수와 같다.
            if(i < coin):
                temp[i] = dp[i]
            else:
                temp[i] = temp[i-coin] + dp[i]

        dp = temp.copy()

    print(dp[m])
