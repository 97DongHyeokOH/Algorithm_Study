import sys

input = sys.stdin.readline


def solution(i, cnt):
    global result
    global button

    if(cnt > len(n)+1):
        return

    result = min(result, cnt+abs(int(i)-int(n)))

    print(result)

    for k in button:
        if(cnt == 0):
            solution(str(k), cnt+1)
        else:
            solution(i+str(k), cnt+1)


n = input().rstrip()

m = int(input())

button = []
br = list(map(int, input().split()))

for i in range(10):
    if(not i in br):
        button.append(i)

result = sys.maxsize

solution('100', 0)

print(result)
