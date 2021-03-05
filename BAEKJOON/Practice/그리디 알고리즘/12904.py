import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

idx = len(t)-1

while(idx >= 0 and s != t[:idx+1]):
    if(t[idx] == 'B'):
        t = t[::-1]
        t = t[1:]
    else:
        t = t[:idx]
    idx = len(t)-1

if(idx == -1):
    print(0)
else:
    print(1)
