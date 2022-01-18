import sys

input = sys.stdin.readline

# f위치에서 t위치로 발을 옮기는데 드는 힘


def move(f, t):
    if(f == t):
        return 1
    elif(f == 0):
        return 2
    elif(abs(f-t) == 2):
        return 4
    else:
        return 3


arr = list(map(int, input().split()))

# dp[i][j][k] -> arr에서 i번째 값으롤 발을 옮기는데 왼발이 j, 오른발이 k인 경우 드는 힘의 최소 값
dp = [[[sys.maxsize]*5 for _ in range(5)] for _ in range(len(arr)-1)]

# 처음(0,0) 발을 옮길 때
dp[0][arr[0]][0] = move(0, arr[0])
dp[0][0][arr[0]] = move(0, arr[0])

for i in range(1, len(arr)-1):
    for l in range(5):
        for r in range(5):
            # 발을 옮길 수 있는 경우
            if(dp[i-1][l][r] != sys.maxsize):
                dp[i][arr[i]][r] = min(
                    dp[i][arr[i]][r], dp[i-1][l][r] + move(l, arr[i]))
                dp[i][l][arr[i]] = min(
                    dp[i][l][arr[i]], dp[i-1][l][r] + move(r, arr[i]))

print(min(map(min, dp[-1])))
