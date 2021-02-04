import sys
from collections import deque as dq

n = int(sys.stdin.readline())
parent = [0]*(n+1)
parent[1] = 1
arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    arr[a].append(b)
    arr[b].append(a)

q = dq([])

for i in arr[1]:
    q.append((1, i))

while(q):
    s, e = q.popleft()

    if(not parent[e]):
        parent[e] = s

    for i in arr[e]:
        if(not parent[i]):
            q.append((e, i))

for i in range(2, n+1):
    print(parent[i])
