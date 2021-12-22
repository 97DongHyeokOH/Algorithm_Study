import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

cities = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if(cities[i][j] == 1):
            houses.append((i, j))
        elif(cities[i][j] == 2):
            chickens.append((i, j))

m_chickens = list(combinations(chickens, m))
result = sys.maxsize

for i in m_chickens:
    temp = 0
    for y, x in houses:
        t = sys.maxsize
        for hy, hx in i:
            t = min(t, abs(hy-y)+abs(hx-x))
        temp += t
    result = min(result, temp)

print(result)
