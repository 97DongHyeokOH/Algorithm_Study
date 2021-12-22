import sys

input = sys.stdin.readline

n, p = map(int, input().split())

finger = [[] for _ in range(6)]
result = 0

for _ in range(n):
    r, pr = map(int, input().split())

    while(finger[r-1] and finger[r-1][-1] > pr):
        finger[r-1].pop()
        result += 1

    if(not finger[r-1] or finger[r-1][-1] < pr):
        finger[r-1].append(pr)
        result += 1

print(result)
