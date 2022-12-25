import sys

input = sys.stdin.readline


def check():
    cnt = 0

    for i in range(n):
        row_cnt = 1
        col_cnt = 1

        for j in range(1, n):
            if candies[i][j] == candies[i][j-1]:
                row_cnt += 1
            else:
                row_cnt = 1

            cnt = max(cnt, row_cnt)

        for j in range(1, n):
            if candies[j][i] == candies[j-1][i]:
                col_cnt += 1
            else:
                col_cnt = 1

            cnt = max(cnt, col_cnt)

    return cnt


n = int(input())

candies = [list(input().rstrip()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if j < n-1:
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            ans = max(ans, check())
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]

        if i < n-1:
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            ans = max(ans, check())
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

print(ans)
