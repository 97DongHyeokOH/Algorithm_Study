import sys
import heapq

input = sys.stdin.readline

n = int(input())

time_table = [list(map(int, input().split())) for _ in range(n)]
time_table.sort()

# 각 회의가 끝나는 시간을 저장 -> 회의가 진행되고 있는 회의실의 수
end_time = []
# 최대 필요 회의실 수
ans = 0

for start, end in time_table:
    # 만약 이번 회의의 시작이간보다 먼저 끝나는 회의가 있으면 해당 회의는 pop해줌
    while end_time and start >= end_time[0]:
        heapq.heappop(end_time)
    
    # 이번 회의가 시작
    heapq.heappush(end_time, end)
    ans = max(ans, len(end_time))

print(ans)