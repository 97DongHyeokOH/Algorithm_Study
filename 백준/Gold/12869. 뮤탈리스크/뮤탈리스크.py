import sys
from itertools import permutations

input = sys.stdin.readline

def solution(cnt, hp1, hp2, hp3):
    if hp1 == 0 and hp2 == 0 and hp3 == 0:
        return
    
    for d1, d2, d3 in list(permutations(damage, 3)):
        h1, h2, h3 = max(0, hp1-d1), max(0, hp2-d2), max(0, hp3-d3)
        if dp[h1][h2][h3] > cnt+1:
            dp[h1][h2][h3] = cnt+1
            solution(cnt+1, h1, h2, h3)

n = int(input())

hp = list(map(int, input().split()))
damage = [9, 3, 1]

while len(hp) < 3:
    hp.append(0)
    
dp = [[[float('inf')]*(hp[2]+1) for _ in range(hp[1]+1)] for _ in range(hp[0]+1)]

solution(0, *hp)

print(dp[0][0][0])