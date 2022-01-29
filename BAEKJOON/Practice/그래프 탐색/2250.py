import sys

input = sys.stdin.readline

# 루트노드를 찾아줌


def find_rootnode():
    rootnode = [True]*(n+1)
    rootnode[0] = False

    for child in tree[1:]:
        if(child[0] != -1):
            rootnode[child[0]] = False
        if(child[1] != -1):
            rootnode[child[1]] = False

    for node in range(n+1):
        if(rootnode[node]):
            return node

# 각 레벨에 몇번의 열번호가 들어가는지 채워준다.


def dfs(node, depth):
    global idx

    if(node == -1):
        return

    dfs(tree[node][0], depth+1)
    depth_arr[depth].append(idx)
    idx += 1
    dfs(tree[node][1], depth+1)


n = int(input())

tree = [0]*(n+1)
# 각 레벨에 어떤 열번호가 들어가는지 저장해주는 리스트
depth_arr = [[] for _ in range(n+1)]
# 열번호
idx = 1
# 결과값
result = [0, 0]

for _ in range(n):
    p, l, r = map(int, input().split())

    tree[p] = [l, r]

# 루트노드에서부터 dfs
dfs(find_rootnode(), 1)

for i in range(n+1):
    if(not depth_arr[i]):
        continue

    width = depth_arr[i][-1]-depth_arr[i][0]+1

    if(result[1] < width):
        result = [i, width]

print(*result)
