import sys

# Union-Find 알고리즘을 이용해 간단히 해결


def Find(x):
    if(x == gate[x]):
        return x
    else:
        gate[x] = Find(gate[x])
        return gate[x]


def Union(x, y):
    x = Find(x)
    y = Find(y)

    gate[x] = y


g = int(sys.stdin.readline())
p = int(sys.stdin.readline())

gate = [i for i in range(g+1)]
cnt = 0

for i in range(p):
    num = int(sys.stdin.readline())
    temp = Find(num)

    if(temp != 0):
        Union(temp, temp-1)
        cnt += 1
    else:
        break

print(cnt)
