import sys


def pos(y, x):
    if(0 <= y < n and 0 <= x < m):
        return True
    return False


def dfs(y, x, cnt):
    global result

    k = int(coin[y][x])
    dy = [k, -k, 0, 0]
    dx = [0, 0, k, -k]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if(pos(ny, nx) and coin[ny][nx] != 'H' and dp[ny][nx] < cnt+1):
            if(visit[ny][nx]):
                print(-1)
                exit(0)
            else:
                dp[ny][nx] = cnt+1
                visit[ny][nx] = True
                dfs(ny, nx, cnt+1)
                visit[ny][nx] = False
        else:
            result = max(result, cnt+1)


n, m = map(int, sys.stdin.readline().split())
coin = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]
result = 0

dfs(0, 0, 0)
print(result)
