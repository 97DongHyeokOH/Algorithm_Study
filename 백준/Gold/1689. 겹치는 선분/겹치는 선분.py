import sys
import heapq

input = sys.stdin.readline

n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]

lines.sort()

end_line = []
cnt = 0
ans = 0

for start, end in lines:
    cnt += 1
    
    while end_line and end_line[0] <= start:
        cnt -= 1
        heapq.heappop(end_line)
    
    heapq.heappush(end_line, end)
    
    ans = max(ans, cnt)

print(ans)