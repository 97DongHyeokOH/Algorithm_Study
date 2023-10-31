import sys
import heapq

input = sys.stdin.readline

n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]
visit = [False]*n
ans = 0
cnt = 0
pos = []

q = [(0, 0, 0)]

while q:
    c, start_node, end_node = heapq.heappop(q)
    
    # print(c, node)
    
    if visit[end_node]:
        if c < 0:
            ans += abs(c)
        continue
    
    ans += abs(c)
    if c > 0:
        cnt += 1
        pos.append(sorted([start_node+1, end_node+1]))
    visit[end_node] = True
    
    for i in range(n):
        if cost[end_node][i] and not visit[i]:
            heapq.heappush(q, (cost[end_node][i], end_node, i))
    
pos.sort()

print(ans, cnt)
for node in pos:
    print(*node)