import copy

# 메인 함수


def solution(info, edges):
    global result

    tree = dict()

    for p, c in edges:
        if(not p in tree):
            tree[p] = [c]
        else:
            tree[p].append(c)

    dfs(0, 0, 0, tree, info, [0])

    return result

# 깊이 우선 탐색
# node -> 현재 노드, sheep -> 현재까지 양의 수, wolf -> 현재까지 늑대의 수
# tree -> 이진 트리를 dictionary로 표현, info -> 문제에서 주어진 2차원 배열


def dfs(node, sheep, wolf, tree, info, parents):
    global result
    temp = copy.deepcopy(parents)

    # 해당 노드에 양이 있는지 늑대가 있는지 확인하고 해당 값을 더함
    if(info[node]):
        wolf += 1
    else:
        sheep += 1

    # 늑대가 양보다 많거나 같아지면 return
    if(sheep <= wolf):
        return

    result = max(result, sheep)

    # parents 배열에 있는 노드들 자식 노드들을 모두 탐색
    for parent_node in parents:
        # 리프 노드인 경우
        if(not parent_node in tree):
            continue
        for child_node in tree[parent_node]:
            if(not visit[child_node]):
                visit[child_node] = True
                temp.append(child_node)
                dfs(child_node, sheep, wolf, tree, info, temp)
                temp.pop()
                visit[child_node] = False


visit = [False]*17
result = 0
