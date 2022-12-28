import sys

input = sys.stdin.readline

m, n = map(int, input().split())

store_cnt = int(input())

store = []

ans = 0

for _ in range(store_cnt):
    direction, distance = map(int, input().split())

    if direction == 1:
        store.append((0, distance, distance))
    elif direction == 2:
        store.append((n, distance, n+m+(m-distance)))
    elif direction == 3:
        store.append((distance, 0, 2*(n+m) - distance))
    else:
        store.append((distance, m, m+distance))

direction, distance = map(int, input().split())

if direction == 1:
    y, x, dist = 0, distance, distance
elif direction == 2:
    y, x, dist = n, distance, n+m+(m-distance)
elif direction == 3:
    y, x, dist = distance, 0, 2*(n+m) - distance
else:
    y, x, dist = distance, m, m+distance

for cy, cx, cdist in store:
    ans += min(abs(dist-cdist), 2*(n+m) - abs(dist-cdist))

print(ans)
