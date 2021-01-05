# Use Sweeping Algorithm

import sys

n = int(sys.stdin.readline().rstrip('\n'))
m = int(sys.stdin.readline().rstrip('\n'))

line = []
result = [0]*m
ans = ''

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())

    if(a > b):
        temp_a = a - n
        temp_b = b + n
        line.append((temp_a, b, i))
        line.append((a, temp_b, i))
    else:
        line.append((a, b, i))

line.sort(key=lambda x: (x[0], -x[1]))
max_end = line[0][1]

for i in line[1:]:
    end = i[1]
    idx = i[2]

    if(end <= max_end):
        result[idx] = 1

    max_end = max(max_end, end)

for idx in range(len(result)):
    if(not result[idx]):
        ans += str(idx+1) + ' '

print(ans)