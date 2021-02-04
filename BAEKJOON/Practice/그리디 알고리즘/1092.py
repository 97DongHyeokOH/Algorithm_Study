import sys

n = int(input())
w = list(map(int, sys.stdin.readline().split()))

m = int(input())
b = list(map(int, sys.stdin.readline().split()))

result = 0

w.sort(reverse=True)
b.sort(reverse=True)

if(w[0] < b[0]):
    print(-1)
    exit()

while(b):
    result += 1

    for idx in range(len(w)):
        for i in range(len(b)):
            if(w[idx] >= b[i]):
                del b[i]
                break

print(result)