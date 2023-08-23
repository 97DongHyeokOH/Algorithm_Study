import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def pos(y, x):
    if 0 <= y < n and 0 <= x < n and not area[y][x]:
        return True
    return False

def go_passenger(y, x):
    dist = [[float('inf')]*n for _ in range(n)]
    
    dq = deque([(0, y, x)])
    dist[y][x] = 0
    temp = []
    min_d = float('inf')
    
    while dq:
        d, cy, cx = dq.popleft()
        
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

passenger_index = defaultdict(int)
done = [False]*m

for i, p in enumerate(passenger):
    passenger_index[(p[0]-1, p[1]-1)] = i+1

cy, cx = start_y-1, start_x-1

while False in done:
    go_p = go_passenger(cy, cx)
    
    if not go_p:
        print(-1)
        exit(0)
    
    go_d = go_destination(*[x - 1 for x in passenger[go_p[3]]])
    
    oil -= go_p[0] + go_d

    if oil < 0:
        print(-1)
        exit(0)
    
    oil += go_d*2
    done[go_p[3]] = True
    cy, cx = [x - 1 for x in passenger[go_p[3]][2:]]

print(oil)