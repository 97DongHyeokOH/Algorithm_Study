import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 세그먼트 트리를 start~end 구간까지 최소값을 가지는 인덱스값으로 초기화 해준다.


def init(node, start, end):
    mid = (start + end) // 2

    if(start == end):
        tree[node] = start
        return

    init(node*2, start, mid)
    init(node*2+1, mid+1, end)

    if(arr[tree[node*2]] < arr[tree[node*2+1]]):
        tree[node] = tree[node*2]
    else:
        tree[node] = tree[node*2+1]

# left~right 구간에서 최소값을 가지는 인덱스를 세그먼트 트리를 통해 찾아준다.


def query(node, start, end, left, right):
    mid = (start + end) // 2

    if(left > end or right < start):
        return -1

    if(start >= left and end <= right):
        return tree[node]

    left_idx = query(node*2, start, mid, left, right)
    right_idx = query(node*2 + 1, mid+1, end, left, right)

    if(left_idx == -1):
        return right_idx
    elif(right_idx == -1):
        return left_idx
    else:
        if(arr[left_idx] >= arr[right_idx]):
            return right_idx
        else:
            return left_idx

# start~end 구간에서 최소값을 가지는 인덱스를 찾아내고 그 인덱스 좌,우로 분할정복한다.


def solution(start, end):
    idx = query(1, 1, arr[0], start, end)

    if(start == end):
        return arr[idx]

    temp1, temp2, temp3 = arr[idx] * (end-start+1), 0, 0

    if(idx-1 >= start):
        temp2 = solution(start, idx-1)
    if(idx+1 <= end):
        temp3 = solution(idx+1, end)

    return max(temp1, temp2, temp3)


while(1):
    arr = list(map(int, input().split()))
    tree = [0]*400001

    if(arr[0] == 0):
        break

    init(1, 1, arr[0])
    print(solution(1, arr[0]))
