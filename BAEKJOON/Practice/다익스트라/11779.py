# 문제: n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라.
# 항상 시작점에서 도착점으로의 경로가 존재한다.

# 입력: 첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다.
# # 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
# 그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.

# 출력: 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
# 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.
# 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.

import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 버스 정류장과 각 도착지로의 비용을 저장해주는 dictionary
bus_station = dict()

# 버스 정류장 출발점 초기화
for i in range(n):
    bus_station[str(i)] = dict()

# 출발지, 도착지, 비용을 받아서 bus_station에 저장해줌
for _ in range(m):
    From, End, Weight = map(int, sys.stdin.readline().split())

    if(str(End-1) in bus_station[str(From-1)]):
        bus_station[str(From-1)][str(End-1)
                                 ] = min(bus_station[str(From-1)][str(End-1)], Weight)
    else:
        bus_station[str(From-1)][str(End-1)] = Weight

# 출발지점과 도착지점
start, end = map(int, sys.stdin.readline().split())

# 도착지까지의 최소비용을 저장해주는 list
cost = [sys.maxsize]*n
cost[start-1] = 0
# 도착지까지 최소비용으로 가게 해주는 루트를 저장해주는 list
route = [[start-1] for _ in range(n)]

# 우선순위 큐 생성
queue = []
heapq.heappush(queue, [start-1, cost[start-1], route[start-1]])

while(queue):
    cur_station, cur_cost, cur_route = heapq.heappop(queue)

    if(cost[cur_station] < cur_cost):
        continue

    for adj, adj_cost in bus_station[str(cur_station)].items():
        c = cur_cost + adj_cost

        # c가 기존의 저장되어있는 비용보다 작으면 cost와 route를 최신화 해주고 우선순위 큐에 넣어준다.
        if(c < cost[int(adj)]):
            cost[int(adj)] = c
            route[int(adj)] = cur_route + [int(adj)]
            heapq.heappush(queue, [int(adj), cost[int(adj)], route[int(adj)]])

# 최소 비용
print(cost[end-1])
# 최소 비용으로 가는데 거치는 정류장 수
print(len(route[end-1]))
# 최소 비용으로 가는 정류장을 순서대로 풀력
for i in route[end-1]:
    print(i+1, end=' ')
