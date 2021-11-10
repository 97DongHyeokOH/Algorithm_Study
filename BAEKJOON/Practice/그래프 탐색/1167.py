import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(i, result):
    for e, d in graph[i]:
        if(result[e] == 0):
            result[e] = result[i] + d
            dfs(e, result)


v = int(input())
graph = [[] for _ in range(v+1)]
for i in range(v):
    path = list(map(int, input().split()))

    path_len = len(path)
    for j in range(1, path_len//2):
        graph[path[0]].append([path[2*j-1], path[2*j]])

result1 = [0]*(v+1)

dfs(1, result1)
result1[1] = 0
temp_max = 0
temp_idx = 0

for i in range(len(result1)):
    if(temp_max < result1[i]):
        temp_max = result1[i]
        temp_idx = i

result2 = [0]*(v+1)
dfs(temp_idx, result2)
result2[temp_idx] = 0
print(max(result2))
