import sys
import heapq


def possible(y, x):
    if(0 <= y < n and 0 <= x < n and miro[y][x] == '1' and not visit[y][x]):
        return True
    return False


def bfs(i, j):
    queue = [(i, j)]
    temp = [(i, j)]

    while(queue):
        y, x = queue.pop(0)

        for idx in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]

            if(possible(ny, nx)):
                queue.append((ny, nx))
                visit[ny][nx] = True
                temp.append((ny, nx))

    return temp


def weight(a, b):
    result = sys.maxsize
    for i in a:
        for j in b:
            result = min(result, abs(i[0] - j[0]) + abs(i[1] - j[1]) - 1)

    return result


n = int(sys.stdin.readline())

miro = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

visit = [[False]*n for _ in range(n)]
nodes = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(n):
    for j in range(n):
        if(miro[i][j] == '1' and not visit[i][j]):
            nodes.append(bfs(i, j))

for i in range(len(nodes)):
    if((0, 0) in nodes[i]):
        start = i

    if((n-1, n-1) in nodes[i]):
        end = i

my_map = dict()

for i in range(len(nodes)):
    my_map[str(i)] = dict()

for i in range(len(nodes)//2 + 1):
    for j in range(i+1, len(nodes)):
        w = weight(nodes[i], nodes[j])
        my_map[str(i)][str(j)] = w
        my_map[str(j)][str(i)] = w

queue = []
dist = [sys.maxsize]*len(nodes)
dist[start] = 0

heapq.heappush(queue, [dist[start], start])

while(queue):
    cur_dist, cur_node = heapq.heappop(queue)

    if(dist[cur_node] < cur_dist):
        continue

    for adj, w in my_map[str(cur_node)].items():
        distance = cur_dist + w

        if(distance < dist[int(adj)]):
            dist[int(adj)] = distance
            heapq.heappush(queue, [distance, int(adj)])

print(dist[end])
