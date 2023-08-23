import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 배열을 벗어나지 않고, 벽을 무시하지 않기 위한 함수
def pos(y, x):
    if 0 <= y < n and 0 <= x < n and not area[y][x]:
        return True
    return False

# 현재 택시가 가장 가까운 승객이 있는 위치까지 가는 함수
def go_passenger(y, x):
    dist = [[float('inf')]*n for _ in range(n)]
    
    dq = deque([(0, y, x)])
    dist[y][x] = 0
    temp = []
    min_d = float('inf')
    
    while dq:
        d, cy, cx = dq.popleft()
        
        # 가장 가까운 승객을 찾으면 그 거리와 같은 승객들은 temp에 넣어두고 행, 열이 가장 낮은 승객에게 간다.
        if d <= min_d and passenger_index[(cy,cx)] and not done[passenger_index[(cy,cx)]-1]:
            temp.append((d, cy, cx, passenger_index[(cy,cx)]-1))
            min_d = d
            continue
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if pos(ny,nx) and dist[ny][nx] > d+1:
                dist[ny][nx] = d+1
                dq.append((d+1, ny, nx))
                
    temp.sort()
    
    if temp:
        return temp[0]
    else:
        return 0

# 승객을 태우고 도착지까지 가는 함수
def go_destination(sy, sx, des_y, des_x):
    dist = [[float('inf')]*n for _ in range(n)]
    
    dq = deque([(0, sy, sx)])
    dist[sy][sx] = 0
    
    while dq:
        d, cy, cx = dq.popleft()
        
        if (cy, cx) == (des_y, des_x):
            return d
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if pos(ny,nx) and dist[ny][nx] > d+1:
                dist[ny][nx] = d+1
                dq.append((d+1, ny, nx))
    
    return float('inf')

n, m, oil = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
start_y, start_x = map(int, input().split())
passenger = [list(map(int, input().split())) for _ in range(m)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 해당 승객을 태웠는지 안태웠는지 판단하기 위함
passenger_index = defaultdict(int)
done = [False]*m

# index에 1을 더해주는 이유는 만약 해당 좌표에 승객이 없으면 defaultdict의 특성상 0을 반환하기 때문에 1을 더해주고, 나중에 index를 통해 승객의 정보를 불러올 때 1을 다시 빼줌
for i, p in enumerate(passenger):
    passenger_index[(p[0]-1, p[1]-1)] = i+1

cy, cx = start_y-1, start_x-1

while False in done:
    go_p = go_passenger(cy, cx)
    
    # 만약 태울 수 있는 승객이 없는 경우
    if not go_p:
        print(-1)
        exit(0)
    
    go_d = go_destination(*[x - 1 for x in passenger[go_p[3]]])
    
    oil -= go_p[0] + go_d

    # 승객을 도착지에 내리기 전에 연료가 다 없어지는 경우
    if oil < 0:
        print(-1)
        exit(0)
    
    oil += go_d*2
    done[go_p[3]] = True
    cy, cx = [x - 1 for x in passenger[go_p[3]][2:]]

print(oil)