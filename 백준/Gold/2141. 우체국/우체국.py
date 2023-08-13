import sys

input = sys.stdin.readline

n = int(input())

info = [list(map(int, input().split())) for _ in range(n)]
info.sort()

total = 0

for _, people in info:
    total += people
    
cur = 0

for i in range(n):
    cur += info[i][1]
    
    if cur >= total/2:
        print(info[i][0])
        break