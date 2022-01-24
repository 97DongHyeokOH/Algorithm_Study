import sys

input = sys.stdin.readline

# 세그먼트 트리를 입력받은 배열로 초기화


def init(node, start, end):
    mid = (start + end) // 2

    if(start == end):
        tree[node] = arr[start]
        return

    init(node*2, start, mid)
    init(node*2+1, mid+1, end)

    tree[node] = min(tree[node*2], tree[node*2+1])

    return tree[node]

# left번째 수에서 right번째 수까지 중 가장 작은 수를 찾아냄


def query(node, start, end, left, right):
    mid = (start + end) // 2

    if(left > end or right < start):
        return sys.maxsize

    if(left <= start and right >= end):
        return tree[node]

    return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))


n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]
# 세그먼트 트리
tree = [0]*(n*4+1)

# 세그먼트 트리 초기화
init(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())

    print(query(1, 1, n, a, b))
