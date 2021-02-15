# 문제 설명
# 도둑이 어느 마을을 털 계획을 하고 있습니다.
# 이 마을의 모든 집들은 동그랗게 배치되어 있습니다.

# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

# 각 집에 있는 돈이 담긴 배열 money가 주어질 때,
# 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
# money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

def solution(money):
    # dp[0]은 첫번째 집을 방문할 때, dp[1]은 첫번째 집을 방문하지 않았을 때
    dp = [[0]*len(money) for _ in range(2)]
    # 3번째 집까지는 직접 계산해준다.
    dp[0][0] = dp[0][1] = money[0]
    dp[0][2] = money[0] + money[2]
    dp[1][0] = 0
    dp[1][1] = money[1]
    dp[1][2] = money[2]

    for i in range(3, len(money)):
        # 첫번째 집을 방문했을때 마지막 집은 방문하면 안된다.
        if(i < len(money)-1):
            dp[0][i] = max(dp[0][i-3], dp[0][i-2]) + money[i]
        dp[1][i] = max(dp[1][i-3], dp[1][i-2]) + money[i]

    return max(max(dp[0]), max(dp[1]))

# 참고 할 만한 풀이
# -> 내 풀이를 더욱 짧고, 간단하게 표현했다.
# -> 메모리도 그렇고 시간도 훨씬 덜 잡아먹을 듯...
# def solution(a):
#     x1, y1, z1 = a[0], a[1], a[0]+a[2]
#     x2, y2, z2 = 0, a[1], a[2]
#     for i in a[3:]:
#         x1, y1, z1 = y1, z1, max(x1, y1)+i
#         x2, y2, z2 = y2, z2, max(x2, y2)+i
#     return max(x1, y1, y2, z2)
