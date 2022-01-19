import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 세그먼트 트리를 배열 값으로 초기화
# 각 노드에는 각 노드에 해당하는(start~end까지)[최솟값, 최댓값]으로 저장을 한다


def init(node, start, end):
    mid = (start + end) // 2

    if(start == end):
        tree[node] = [arr[start], arr[start]]
        return

    init(node*2, start, mid)
    init(node*2+1, mid+1, end)

    tree[node][0] = min(tree[node*2][0], tree[node*2+1][0])
    tree[node][1] = max(tree[node*2][1], tree[node*2+1][1])

# 해당되는 범위에서의 최솟값, 최댓값을 찾아준다.


def query(node, start, end, left, right):
    mid = (start + end) // 2

    if(left > end or right < start):
        return [sys.maxsize, -1]

    if(left <= start and right >= end):
        return tree[node]

    temp1 = (query(node*2, start, mid, left, right))
    temp2 = (query(node*2+1, mid+1, end, left, right))

    return [min(temp1[0], temp2[0]), max(temp1[1], temp2[1])]


arr = [int(input()) for _ in range(n)]

# 세그먼트 트리
tree = [[0, 0] for _ in range(400001)]

# 세그먼트 트리 초기화
init(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())

    print(*query(1, 1, n, a, b))
