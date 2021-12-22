import sys

input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 1

while(a < b):
    if(str(b)[-1] == '1'):
        b = int(str(b)[:-1])
        cnt += 1
    elif(int(str(b)[-1]) % 2 == 0):
        b = int(b//2)
        cnt += 1
    else:
        cnt = -1
        break

if(a == b):
    print(cnt)
else:
    print(-1)
