import sys

n = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

# dp[i] -> 무게가 i인 구술의 무게를 확인할수 있는지 판단
dp = [False]*40001
dp[0] = True

for w in weight:
    temp = dp.copy()
    for i in range(40001):
        if(dp[i]):
            if(i+w < 40001):
                temp[i+w] = True
            temp[abs(i-w)] = True
    dp = temp.copy()

for c in check:
    if(dp[c]):
        print('Y', end=' ')
    else:
        print('N', end=' ')
