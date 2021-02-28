import sys

n, c = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

left = 1
right = 1000000000
result = 0

while(left <= right):
    mid = (left + right) // 2
    cnt = 1
    length = 0

    for idx in range(1, len(arr)):
        length += (arr[idx] - arr[idx-1])

        if(length >= mid):
            cnt += 1
            length = 0

    if(cnt >= c):
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1

print(result)
