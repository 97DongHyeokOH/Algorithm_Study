import sys

n, m = map(int, sys.stdin.readline().split())

bead = list(map(int, sys.stdin.readline().split()))

left = min(bead)
right = 30000
result = -1
result_num = []

while(left <= right):
    mid = (left + right) // 2

    temp = 0
    num_cnt = 0
    num = []
    cnt = 0
    check = True

    for i in range(len(bead)):
        if(mid < max(bead)):
            cnt = -1
            break
        temp += bead[i]
        num_cnt += 1

        if(len(bead) - i == m - len(num)):
            check = False
            print(num, i)
            while(m - len(num)):
                cnt += 1
                num.append('1')
            break
        elif(temp > mid):
            cnt += 1
            temp = bead[i]
            num.append(str(num_cnt-1))
            num_cnt = 1

    if(check):
        num.append(str(num_cnt))
        cnt += 1

    print(left, right, mid)
    print(cnt)
    print(num)

    if(cnt > m or not cnt):
        left = mid + 1
    else:
        if(cnt == m):
            result = mid
            result_num = num
        right = mid - 1


print(result)
print(' '.join(result_num))
