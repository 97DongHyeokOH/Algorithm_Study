import sys
import heapq


def solution(n, start, end, roads, traps):
    my_map = dict()

    for i in range(n):
        my_map[str(i)] = dict()

    for road in roads:
        f, t, w = road
        my_map[str(f-1)][str(t-1)] = [w, 1]
        my_map[str(t-1)][str(f-1)] = [w, 0]

    queue = []
    dist = [sys.maxsize]*n
    dist[start-1] = 0

    heapq.heappush(queue, [dist[start-1], start-1])

    while(queue):
        cur_dist, cur_node = heapq.heappop(queue)
        temp = []

        if(cur_node == end-1):
            break

        for adj, d in my_map[str(cur_node)].items():
            if(d[1] == 0):
                continue

            distance = cur_dist + d[0]

            dist[int(adj)] = min(distance, dist[int(adj)])
            heapq.heappush(queue, [distance, int(adj)])

            if((int(adj)+1) in traps):
                temp.append(adj)

        for i in temp:
            for t_adj, t_d in my_map[i].items():
                my_map[i][t_adj][1] = (my_map[i][t_adj][1] + 1) % 2
                my_map[t_adj][i][1] = (my_map[t_adj][i][1] + 1) % 2

    return dist[end-1]


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
