import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([min(a, b), max(a, b)])
d = int(input())
result = 0

arr.sort(key=lambda x: x[1])
queue = []

for i in range(n):
    start, end = arr[i]

    if(end-start <= d):
        heapq.heappush(queue, start)

    while(queue and queue[0] < end-d):
        heapq.heappop(queue)

    result = max(result, len(queue))

print(result)
