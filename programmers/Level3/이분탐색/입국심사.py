def solution(n, times):
    left = 1
    right = n * min(times)
    result = 0

    while(left <= right):
        mid = (left + right) // 2
        temp = 0

        for time in times:
            temp += mid // time
            if(temp >= n):
                result = mid
                right = mid-1
                break

        if(temp < n):
            left = mid+1

    return result


print(solution(6, [7, 10]))
