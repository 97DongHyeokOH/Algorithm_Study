import sys

sys.setrecursionlimit(100000) # 재귀한도를 풀어준다.

def sol(i):
    if(not arr[i]):
        return dp[i]
    
    while(arr[i]):
        j = arr[i].pop()

        dp[i] = max(dp[i], sol(j) + time[i])
    
    return dp[i]


t = int(sys.stdin.readline())

for _ in range(t):
    n,k = map(int, sys.stdin.readline().split())

    time = list(map(int, sys.stdin.readline().split()))
    arr = [[] for j in range(n)]
    dp = [time[idx] for idx in range(n)]

    for i in range(k):
        a,b = map(int, sys.stdin.readline().split())
        arr[b-1].append(a-1)
    
    dest = int(sys.stdin.readline())

    print(sol(dest-1))