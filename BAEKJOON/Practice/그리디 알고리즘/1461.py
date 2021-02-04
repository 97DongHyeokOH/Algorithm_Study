import sys

n,m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

neg = []
pos = []
step = []

for i in arr:
    if(i < 0):
        neg.append(abs(i))
    elif(i > 0):
        pos.append(i)

neg.sort()
pos.sort()

temp = 0
k = 0

while(neg):
    num = neg.pop()
    if(k == 0):
        temp += num
    k += 1

    if(k == m or not neg):
        step.append(temp)
        temp = 0
        k = 0

while(pos):
    num = pos.pop()
    if(k == 0):
        temp += num
    k += 1

    if(k == m or not pos):
        step.append(temp)
        temp = 0
        k = 0

step.sort()
result = 0

for i in step:
    result += i*2

result -= step[len(step)-1]

print(result)