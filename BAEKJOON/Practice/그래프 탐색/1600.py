import sys
import heapq

input = sys.stdin.readline

# 원숭이가 움직인 위치가 배열을 벗어나지않고, 벽이 아닌지 판단
def pos(y, x):
    if 0 <= y < h and 0 <= x < w and board[y][x] == 0:
        return True
    return False

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

# 일반적으로 움직이는 경우와, 말처럼 움직이는 경우의 위치 변화
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
horse_dy = [-2, -2, -1, -1, 1, 1, 2, 2]
horse_dx = [-1, 1, -2, 2, -2, 2, -1, 1]
# visit[i][j][k] -> (i,j)위치에 말 처럼움직인 횟수가 k번인 경우 방문했는지 판단
visit = [[[False]*(k+1) for _ in range(w)] for _ in range(h)]

# 최소힙과 bfs를 이용해 문제를 해결
queue = [(0, 0, 0, 0)]
visit[0][0][0] = True

while queue:
    cnt, horse_cnt, y, x = heapq.heappop(queue)

    # 만약 오른쪽 제일 아래라면 움직인 횟수를 출력하고 종료
    if y == h-1 and x == w-1:
        print(cnt)
        exit(0)
    
    # 일반적으로 움직이는 경우
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if pos(ny, nx) and not visit[ny][nx][horse_cnt]:
            heapq.heappush(queue, (cnt+1, horse_cnt, ny, nx))
            visit[ny][nx][horse_cnt] = True

    # 말처럼 움직일 수 있는 횟수를 넘어서면 말처럼은 못 움직인다.
    if horse_cnt == k:
        continue

    # 말처럼 움직이는 경우
    for i in range(8):
        ny = y + horse_dy[i]
        nx = x + horse_dx[i]

        if pos(ny, nx) and not visit[ny][nx][horse_cnt+1]:
            heapq.heappush(queue, (cnt+1, horse_cnt+1, ny, nx))
            visit[ny][nx][horse_cnt+1] = True

# 도착지에 도착할 수 있는 경우의 수가 없다.
print(-1)