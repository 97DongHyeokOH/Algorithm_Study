import sys

input = sys.stdin.readline

n, score, p = map(int, input().split())

if n <= 0:
    print(1)
    exit(0)

rank = list(map(int, input().split()))

rank.append(score)
rank.sort(reverse=True)

rank_list = []
result = 0

for i in range(n+1):
    if len(rank_list) < p:
        rank_list.append(rank[i])

        if rank[i] == score:
            if not result:
                result = i+1
    else:
        if rank[i] >= score:
            result = -1
            break

print(result)
