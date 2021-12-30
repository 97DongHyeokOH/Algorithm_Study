import sys

input = sys.stdin.readline


def update(node, start, end, i, idx):
    mid = (start + end) // 2

    if(idx < start or idx > end):
        return

    tree[node] += i

    if(start != end):
        update(node * 2, start, mid, i, idx)
        update(node * 2 + 1, mid+1, end, i, idx)


def query(node, start, end, seq):
    mid = (start + end) // 2

    if(start == end):
        return start

    if(tree[node*2] >= seq):
        return query(node*2, start, mid, seq)
    else:
        return query(node*2 + 1, mid+1, end, seq - tree[node*2])


n = int(input())

temp = [list(map(int, input().split())) for _ in range(n)]

tree = [0]*4000011
arr = [0]*1000001

for i in temp:
    if(i[0] == 1):
        ans = query(1, 1, 1000000, i[1])
        print(ans)
        arr[ans] -= 1
        update(1, 1, 1000000, -1, ans)
    else:
        arr[i[1]] += i[2]
        update(1, 1, 1000000, i[2], i[1])
