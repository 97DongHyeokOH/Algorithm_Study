import sys


def solution(distance, rocks, n):
    left = 0
    right = distance
    length = 0
    answer = 0

    rocks.sort()
    rocks.append(distance)

    while(left <= right):
        mid = (left + right) // 2
        result = sys.maxsize
        start = 0
        cnt = 0

        for i in rocks:
            length = i - start
            if(length < mid):
                cnt += 1
            else:
                start = i
                result = min(result, length)

        if(cnt > n):
            right = mid - 1
        else:
            answer = result
            left = mid + 1

    return answer


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

print(solution(distance, rocks, n))
