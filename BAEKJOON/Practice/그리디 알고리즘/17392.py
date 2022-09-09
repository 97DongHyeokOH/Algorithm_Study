import sys

input = sys.stdin.readline

n, m = map(int, input().split())

sum_vac = min(sum(map(int, input().split())) + n, m)
temp = [0]

for i in range(1, 1001):
    temp.append(temp[i-1] + i**2)

share = (m-sum_vac) // (n+1)
rest = (m-sum_vac) % (n+1)

print((temp[share] * (n+1-rest)) + ((temp[share+1]) * rest))
