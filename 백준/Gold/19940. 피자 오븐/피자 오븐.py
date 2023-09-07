import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    ans = [n // 60, 0, 0, 0, 0]
    n %= 60
    
    if n % 10 > 5 or (n % 10 >= 5 and n // 10 > 3):
        ans[4] += 10 - n % 10
        n += 10 - n % 10
    else:
        ans[3] += n % 10
        n -= n % 10
    
    if n == 60:
        ans[0] += 1
    elif n > 30:
        ans[0] += 1
        ans[2] += 6 - n // 10
    else:
        ans[1] += n // 10
    
    print(*ans)