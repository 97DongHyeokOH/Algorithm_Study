import sys
from collections import defaultdict

input = sys.stdin.readline

def solution(i):
    if dp[i]:
        return dp[i]
    
    ip = i // p
    iq = i // q
    
    dp[i] += solution(ip)
    dp[i] += solution(iq)
    
    return dp[i]
    
n, p, q = map(int, input().split())

# dp를 배열로 만들면 10^12크기의 배열이 필요 -> 메모리가 너무 많이 필요
# dictionary로 필요한 값들만 저장
dp = defaultdict(int)

dp[0] = 1

print(solution(n))