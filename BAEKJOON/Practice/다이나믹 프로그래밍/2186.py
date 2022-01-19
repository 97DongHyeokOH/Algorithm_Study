from re import L
import sys

input = sys.stdin.readline

# 배열을 안 벗


def pos(y, x):
    if(0 <= y < n and 0 <= x < m):
        return True
    return False


n, m, k = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

s = input().rstrip()

# dp[i][j][k] -> 문자열의 i번째 문자가 j열 ,k행에서
dp = [[[0]*m for _ in range(n)] for _ in range(len(s))]

# 상하좌우로 움직이기
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

# temp_dict[c] -> c문자가 있는 위치
temp_dict = dict()

# dp[0]과 temp_dict 값을 초기화 해줌.
for y in range(n):
    for x in range(m):
        if(arr[y][x] == s[0]):
            dp[0][y][x] = 1

        if(arr[y][x] in temp_dict):
            temp_dict[arr[y][x]].append((y, x))
        else:
            temp_dict[arr[y][x]] = [(y, x)]

for i in range(len(s)-1):
    for y, x in temp_dict[s[i]]:
        for j in range(k):
            for l in range(4):
                ny = y + dy[l]*(j+1)
                nx = x + dx[l]*(j+1)

                if(pos(ny, nx) and arr[ny][nx] == s[i+1]):
                    dp[i+1][ny][nx] += dp[i][y][x]

result = 0

for i in range(n):
    result += sum(dp[len(s)-1][i])

print(result)
