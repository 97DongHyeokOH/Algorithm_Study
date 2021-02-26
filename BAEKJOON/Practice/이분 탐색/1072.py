import sys


def rate(x, y):
    return int(y * 100 / x)


x, y = map(int, sys.stdin.readline().split())
z = rate(x, y)
result = sys.maxsize+1

if(z >= 99):
    print(-1)
    exit()

start = 0
end = sys.maxsize

while(start <= end):
    mid = (start + end) // 2

    if(z < rate(x+mid, y+mid)):
        result = min(result, mid)
        end = mid - 1
    else:
        start = mid + 1

print(result)
