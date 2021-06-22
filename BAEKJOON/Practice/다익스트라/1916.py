# 문제: N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

# 입력: 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다.
# 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
# 그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

# 출력: 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 출발지 -> 도착지 비용 저장하는 dictionary
my_map = dict()

# 각 출발지를 dict으로 초기화
for i in range(n):
    my_map[str(i)] = dict()

# 입력을 받아서 my_map에 저장
for i in range(m):
    d, a, c = map(int, sys.stdin.readline().split())

    if(str(a-1) in my_map[str(d-1)]):
        my_map[str(d-1)][str(a-1)] = min(my_map[str(d-1)][str(a-1)], c)
    else:
        my_map[str(d-1)][str(a-1)] = c

# 출발지점, 도착지점 입력 받음
depart, arrive = map(int, sys.stdin.readline().split())

queue = []  # 우선순위 큐

# 시작점으로부터 각 도착점까지의 최소비용을 저장해주는 list
cost = [sys.maxsize]*n
cost[depart-1] = 0

# 우선순위 큐를 활용한 다익스트라 알고리즘
heapq.heappush(queue, [cost[depart-1], depart-1])

while(queue):
    cur_cost, cur_node = heapq.heappop(queue)

    if(cost[cur_node] < cur_cost):
        continue

    for adj, c in my_map[str(cur_node)].items():
        c += cur_cost

        if(c < cost[int(adj)]):
            cost[int(adj)] = c
            heapq.heappush(queue, [c, int(adj)])

print(cost[arrive-1])
