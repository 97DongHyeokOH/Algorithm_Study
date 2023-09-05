import sys
from collections import deque

def pos(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False

input = sys.stdin.readline

n, m = map(int, input().split())

farm = [list(map(int, input().split())) for _ in range(n)]

visit = [[False]*m for _ in range(n)]

cnt = 0

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

for y in range(n):
    for x in range(m):
        if visit[y][x]:
            continue
        
        h = farm[y][x]
        queue = deque([(y, x)])
        visit[y][x] = True
        mountaintop = []
        
        can_top = True
        
        while queue:
            cy, cx = queue.popleft()
            
            mountaintop.append((cy,cx))
            
            for i in range(8):
                ny = cy + dy[i]
                nx = cx + dx[i]
                
                if pos(ny,nx) and not visit[ny][nx] and farm[ny][nx] == h:
                    queue.append((ny,nx))
                    visit[ny][nx] = True
                    
        for cy, cx in mountaintop:
            for i in range(8):
                ny = cy + dy[i]
                nx = cx + dx[i]
                
                if pos(ny,nx) and farm[ny][nx] > h:
                    can_top = False
        
        if can_top:
            cnt += 1
            
print(cnt)