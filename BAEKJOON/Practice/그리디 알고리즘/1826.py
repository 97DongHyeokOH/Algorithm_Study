import sys
import heapq

input = sys.stdin.readline

n = int(input())
oil_station = [list(map(int, input().split())) for _ in range(n)]

# 가까운 거리순으로 정렬
oil_station.sort()

# 마을 위치, 현재 기름으로 갈 수 있는 거리(출발지에서 부터)
village, cur_oil = map(int, input().split())
# 현재 주유소 전까지 주유소들의 연료 양(최대 힙으로 활용하기 위해 음수로 되어있음)
queue = []
# 주유소를 방문한 횟수
cnt = 0

for dist, oil in oil_station:
    while dist > cur_oil:
        if not queue:
            print(-1)
            exit(0)

        cur_oil -= heapq.heappop(queue)
        cnt += 1

    heapq.heappush(queue, -oil)

while village > cur_oil:
    if not queue:
        print(-1)
        exit(0)

    cur_oil -= heapq.heappop(queue)
    cnt += 1

print(cnt)
