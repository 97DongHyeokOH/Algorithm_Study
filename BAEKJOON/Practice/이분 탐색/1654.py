import sys


def binary_search(start, end):
    result = 0

    while(start <= end):
        mid = (start + end) // 2
        cnt = 0

        for length in pipe:
            cnt += (length // mid)

        if(cnt >= n):
            result = max(result, mid)
            start = mid + 1
        else:
            end = mid - 1

    return result


k, n = map(int, sys.stdin.readline().split())

pipe = []

for _ in range(k):
    pipe.append(int(sys.stdin.readline()))

print(binary_search(1, sys.maxsize))
