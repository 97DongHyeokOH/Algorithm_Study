import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())

    cost = sorted(list(map(int, input().split())))
    result = 0

    while len(cost) > 1:
        c1 = heapq.heappop(cost)
        c2 = heapq.heappop(cost)

        result += c1 + c2

        heapq.heappush(cost, c1+c2)

    print(result)
