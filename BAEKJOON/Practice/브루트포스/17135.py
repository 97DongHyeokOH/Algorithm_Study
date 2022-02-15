import sys
from itertools import combinations

input = sys.stdin.readline

n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 궁수가 있을수 있는 위치를 조합으로 구해줌
archers = list(combinations([i for i in range(m)], 3))
# dist[i] -> 궁수가 i위치에 있을 때, 모든 적에 대해서 (거리, x좌표 , y좌표)로 저장하는 list
dist = [[] for _ in range(m)]
# 결과값
result = 0

for y in range(n):
    for x in range(m):
        if(arr[y][x]):
            for i in range(m):
                distance = n-y + abs(i-x)
                dist[i].append((distance, x, y))

# 거리, x좌표, y좌표 기준으로 오름차순 정렬해준다.
for i in range(m):
    dist[i].sort()

# 모든 적들의 수
enemies = len(dist[0])

# 모든 경우에 대해 최대값을 찾아준다.
for archer in archers:
    # 쏜 적의 좌표
    shoot = set()
    # idx[i] -> i번 궁수가 자신의 dist에서 쏠 수 있는 인덱스를 저장해줌
    idx = [0, 0, 0]
    # 턴은 최대 n번까지 돌 수 있다.
    for turn in range(n):
        # 이번턴에 잡은 적
        cur_turn = set()
        # 3명의 궁수가 1명의 적을 공격(중복가능)
        for i in range(3):
            while(idx[i] < enemies):
                distance, x, y = dist[archer[i]][idx[i]]
                # 거리가 안돼서 쏠 수 있는 적이 없으면 이번턴은 그냥 넘어간다
                if(distance - turn > d):
                    break
                # 이미 죽인 적이거나 성이 있는 칸으로 들어온 적인 경우
                if((y, x) in shoot or y+turn >= n):
                    idx[i] += 1
                    continue

                cur_turn.add((y, x))
                idx[i] += 1
                break

        shoot = shoot.union(cur_turn)

    result = max(result, len(shoot))

print(result)
