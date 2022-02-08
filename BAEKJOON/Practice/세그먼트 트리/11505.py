import sys

input = sys.stdin.readline

# 세그먼트 트리를 초기화


def init(node, start, end):
    mid = (start + end) // 2

    if(start == end):
        tree[node] = arr[start]
        return

    init(node*2, start, mid)
    init(node*2+1, mid+1, end)

    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007

    return tree[node]

# 세그먼트 트리를 업데이트


def update(node, start, end, i, k):
    mid = (start + end) // 2

    if(i < start or i > end):
        return 1

    if(start != end):
        update(node*2, start, mid, i, k)
        update(node*2+1, mid+1, end, i, k)
    elif(start == i):
        tree[node] = k
        return tree[node]

    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007

    return tree[node]

# left부터 right까지의 곱을 구해준다.


def query(node, start, end, left, right):
    mid = (start + end) // 2

    if(left > end or right < start):
        return 1

    if(left <= start and right >= end):
        return tree[node]

    return (query(node*2, start, mid, left, right) * query(node*2+1, mid+1, end, left, right)) % 1000000007


n, m, k = map(int, input().split())

tree = [0]*(4*n+1)

arr = [int(input()) for _ in range(n)]

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())

    if(a == 1):
        update(1, 0, n-1, b-1, c)
        arr[b-1] = c
    else:
        print(query(1, 0, n-1, b-1, c-1))
