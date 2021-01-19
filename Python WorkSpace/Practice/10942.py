import sys

def palindrome(s,e):
    while(s < e):
        if(arr[s] != arr[e]):
            return False
        s += 1
        e -= 1
    return True

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        start = i
        end = j
        if(not dp[start][end] and palindrome(start,end)):
            while(start <= end):
                dp[start][end] = 1
                start += 1
                end -= 1

for _ in range(m):
    s,e = map(int, sys.stdin.readline().split())

    print(dp[s-1][e-1])