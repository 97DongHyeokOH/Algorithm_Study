import sys


def solution(turn, left, right):
    if(left > right):
        return 0

    # 이미 dp에 값이 들어가 있다면 바로 return
    if(dp[left][right]):
        return dp[left][right]

    # 근우의 턴인 경우 자신이 왼쪽, 오른쪽 카드 중 하나를 선택한 뒤에 나머지 카드를 뽑는 경우중에 최대값을 선택
    if(turn % 2):
        dp[left][right] = max(arr[left] + solution(turn+1, left+1, right),
                              arr[right] + solution(turn+1, left, right-1))
    # 명우의 턴인 경우 자신이 왼쪽, 오른쪽 카드 중 하나를 선택한 뒤에 근우가 최소한으로 카드를 얻게 하는 수를 선택
    else:
        dp[left][right] = min(solution(turn+1, left+1, right),
                              solution(turn+1, left, right-1))

    return dp[left][right]


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    # dp[i][j] -> i번째 카드부터 j번째 카드까지 근우가 얻을수 있는 점수의 최대 값
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # 재귀 함수와 dp배열을 통해 풀어준다.
    solution(1, 0, n-1)
    # 첫번째 카드부터 마지막 카드까지 근우가 얻을 수 있는 최대 값
    print(dp[0][n-1])
