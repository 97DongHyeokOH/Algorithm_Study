import sys

input = sys.stdin.readline

# 배열을 벗어나는지 판단


def pos(y, x):
    if(0 <= y < n and 0 <= x < m and paper[y][x]):
        return True
    return False


n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]

# 배열을 방문했는지 저장하는 list
visit = [[False]*m for _ in range(n)]
# 최대 그림 면적
result = 0
# 그림의 수
result_cnt = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        # 그림이 있고 방문하지 않았다면 bfs를 해준다.
        if(paper[i][j] and not visit[i][j]):
            queue = [(i, j)]
            visit[i][j] = True
            cnt = 1

            while(queue):
                y, x = queue.pop(0)

                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if(pos(ny, nx) and not visit[ny][nx]):
                        queue.append((ny, nx))
                        visit[ny][nx] = True
                        cnt += 1

            result = max(result, cnt)
            result_cnt += 1

print(result_cnt)
print(result)
