import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

while 1:
    m, n = map(int, input().split())
    total = 0
    ans = 0
    
    if m == 0 and n == 0:
        break
    
    graph = defaultdict(lambda : defaultdict(int))
    visit = [False]*m
    
    for _ in range(n):
        n1, n2, cost = map(int, input().split())
        total += cost
        
        graph[n1][n2] = cost
        graph[n2][n1] = cost
    
    q = []
    
    for node in graph[0].keys():
        heapq.heappush(q, (graph[0][node], node))
        
    visit[0] = True
    
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        
        if visit[cur_node]:
            continue
        
        visit[cur_node] = True
        ans += cur_cost
        
        for node in graph[cur_node].keys():
            heapq.heappush(q, (graph[cur_node][node], node))
            
    print(total - ans)