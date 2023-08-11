import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

castle = [list(map(int, input().split())) for _ in range(m)]

room = [[0]*n for _ in range(m)]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

# 방에 숫자를 붙여준다
room_num = 1
# 방의 넓이와 연결된 방의 숫자를 저장한다
room_state = {}
# 최대 방 넓이
max_room = 0
# 2개의 방이 합쳐진 경우 최대 넓이
max_two_room = 0

for y in range(m):
    for x in range(n):
        # 이미 방에 숫자가 붙여져 있다면 넘김
        if room[y][x]:
            continue
        
        # 숫자가 없는 방의 경우 bfs를 통해 연결된 모든 방을 구해주고,
        # 벽을 부수면 연결되는 방도 room_state에 저장해준다.
        queue = deque([(y,x)])
        room[y][x] = room_num
        room_state[room_num] = {}
        room_state[room_num]['connect'] = set()
        cnt = 1
        
        while queue:
            cur_y, cur_x = queue.popleft()
            cur_state = castle[cur_y][cur_x]
            
            for i in range(4):
                ny = cur_y + dy[i]
                nx = cur_x + dx[i]
                if not cur_state % 2 and not room[ny][nx]:
                    room[ny][nx] = room_num
                    queue.append((ny,nx))
                    cnt += 1
                else:
                    if 0 <= ny < m and 0 <= nx < n and room[ny][nx] and room[ny][nx] != room_num:
                        room_state[room_num]['connect'].add(room[ny][nx])
                    
                cur_state //= 2
        
        room_state[room_num]['cnt'] = cnt
        max_room = max(max_room, cnt)
        room_num += 1
        
for first_room in room_state.keys():
    for second_room in room_state[first_room]['connect']:
        two_room = room_state[first_room]['cnt'] + room_state[second_room]['cnt']
        max_two_room = max(max_two_room, two_room)
    
print(room_num-1)
print(max_room)
print(max_two_room)