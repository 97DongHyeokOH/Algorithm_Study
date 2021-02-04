import sys

n,m = map(int, sys.stdin.readline().split())

if(n == 1 or m == 1):
    print(1)
elif(n == 2):
    if(m >= 7):
        print(4)
    else:
        print(1+ (m-1) // 2)
elif(m < 5):
    print(m)
elif(m < 7):
    print(4)
else:
    print(5 + (m-7))