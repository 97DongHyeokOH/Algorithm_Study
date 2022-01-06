import sys

input = sys.stdin.readline

n = int(input())

arr = [[] for _ in range(4)]
max_num = 2**28
result = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    arr[3].append(d)

for i in range(4):
    arr[i].sort()

temp1, temp2 = [], dict()

for i in range(n):
    for j in range(n):
        temp1.append(arr[0][i] + arr[1][j])
        num = arr[2][i] + arr[3][j]
        if(num in temp2):
            temp2[num] += 1
        else:
            temp2[num] = 1

temp1.sort()

for i in temp1:
    if(-i in temp2):
        result += temp2[-i]

print(result)
