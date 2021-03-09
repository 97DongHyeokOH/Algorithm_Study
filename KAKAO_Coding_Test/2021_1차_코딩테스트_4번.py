import sys
from collections import deque as dq

# 다익스트라(Dijkstra) 알고리즘 인지 후 2일차 도전


def solution(n, s, a, b, fares):
    result = sys.maxsize
    maps = [[sys.maxsize]*n for _ in range(n)]
    distance = []

    for f in fares:
        maps[f[0]-1][f[1]-1] = f[2]
        maps[f[1]-1][f[0]-1] = f[2]

    for i in range(n):
        maps[i][i] = 0

    # 다익스트라 알고리즘
    # i 노드에서 출발했을 때, 각 노드별 최단 거리 구하기
    def go(i):
        dis = [0]*n
        visit = [False]*

        # 값이 최소인 index 찾기
        def get_small():
            num = sys.maxsize
            idx = 0

            for k in range(n):
                if(dis[k] < num and not visit[k]):
                    num = dis[k]
                    idx = k

            return idx

        for j in range(n):
            dis[j] = maps[i][j]

        visit[i] = True

        for j in range(n-2):
            cur_idx = get_small()
            visit[cur_idx] = True
            for k in range(n):
                if(not visit[k]):
                    if(dis[cur_idx] + maps[cur_idx][k] < dis[k]):
                        dis[k] = dis[cur_idx] + maps[cur_idx][k]

        return dis

    for i in range(n):
        distance.append(go(i))

    for i in range(n):
        result = min(result, distance[s-1][i] +
                     distance[i][a-1] + distance[i][b-1])

    return result

# 정답란에 있던 참고하기 좋은 코드
# def solution(n, s, a, b, fares):
#     d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
#     for x in range(n):
#         d[x][x] = 0
#     for x, y, c in fares:
#         d[x-1][y-1] = c
#         d[y-1][x-1] = c

#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if d[j][k] > d[j][i] + d[i][k]:
#                     d[j][k] = d[j][i] + d[i][k]

#     minv = 40000002
#     for i in range(n):
#         minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
#     return minv
