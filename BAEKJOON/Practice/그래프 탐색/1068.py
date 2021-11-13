import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(i, j):
    if(i == node):
        j = False
    elif(tree[i] == [node]):
        result[i] = 1
    elif(not tree[i] and j):
        result[i] = 1

    for k in tree[i]:
        dfs(k, j)


n = int(input())

parent = list(map(int, input().split()))

node = int(input())

tree = [[] for _ in range(n)]
result = [0]*n

for i in range(n):
    if(parent[i] != -1):
        tree[parent[i]].append(i)

dfs(parent.index(-1), True)

print(sum(result))
