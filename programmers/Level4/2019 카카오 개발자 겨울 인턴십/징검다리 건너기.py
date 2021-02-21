def solution(stones, k):
    start = 1
    end = 200000000  # 2억

    while(start < end):
        mid = (start + end) // 2

        cnt = 0
        result = 0

        for i in stones:
            if(i <= mid):
                cnt += 1
            else:
                cnt = 0
            result = max(cnt, result)

        if(result >= k):
            end = mid
        else:
            start = mid+1

    return start
