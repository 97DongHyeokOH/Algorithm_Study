import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())

info = [list(map(lambda x: -x, list(map(int, input().split())))) + [i % m] for i in range(n)]

queue = info[:min(m, len(info))]
heapq.heapify(queue)
line_cnt = [0]*m
cnt = 0

while queue:
    d, h, i = heapq.heappop(queue)
    
    cur_num = i + m * line_cnt[i]
    line_cnt[i] += 1
    
    if cur_num == k:
        break
    
    if cur_num + m < n:
        heapq.heappush(queue, info[cur_num + m])
        
    cnt += 1

print(cnt)