import sys
from collections import deque

input = sys.stdin.readline

# 배열을 벗어나는지 판단하는 함수
def pos(y,x):
    if(0 <= y < n and 0 <= x < m):
        return True
    return False

# 상,하,좌,우 움직이는 방향
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    # 양배추가 어느 좌표에 있는지 저장하는 list
    cabbages = []
    # 배추밭
    arr = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())

        # 배추밭에 배추가 있는 위치에 1을 넣어주고, 배추가 어느 좌표에 있는지 추가해준다.
        arr[y][x] = 1
        cabbages.append((y,x))

    # 방문한 좌표인지 확인을 위한 list
    visit = [[False]*m for _ in range(n)]
    # 필요한 지렁이의 수
    cnt = 0

    # bfs를 이용해 해결
    for y, x in cabbages:
        # 방문하지 않은 좌표하면 bfs를 통해 연결된 배추들을 뽑아낸다.
        if(not visit[y][x]):
            dq = deque([(y,x)])
            visit[y][x] = True

            while(dq):
                cur_y, cur_x = dq.popleft()

                for i in range(4):
                    ny = cur_y + dy[i]
                    nx = cur_x + dx[i]
                    
                    # 배추밭은 벗어나지 않는지, 방문하지 않은 좌표인지, 배추가 있는곳인지 확인을 한다.
                    if(pos(ny,nx) and not visit[ny][nx] and arr[ny][nx]):
                        visit[ny][nx] = True
                        dq.append((ny,nx))
            
            cnt += 1
    
    print(cnt)