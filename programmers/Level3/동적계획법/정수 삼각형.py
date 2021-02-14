# 위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중,
# 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
# 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다.
# 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때,
# 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

# 제한사항
# 삼각형의 높이는 1 이상 500 이하입니다.
# 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

import copy


def solution(triangle):
    # 2차원 이상의 배열에서는 copy.deepcopy()인 '깊은 복사'를 해야 제대로 복사된다
    # list와 dictionary같은 경우 mutable(값이 변할 수 있음)이기 때문에 리스트의 [:]나 deepcopy
    # 함수를 이용하면 같은 주소 값을 가르키지 않게 된다.
    dp = copy.deepcopy(triangle)
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

    return max(dp[len(triangle)-1])
