def solution(lines):
    answer = 0
    # lines에 있는 값으로 (시작시간, 끝나는시간)을 ms단위로 저장하는 list
    temp = []
    for line in lines:
        day, time, treat = line.split()
        hour, minute, second = map(float, time.split(':'))
        second = int(second*1000)
        second += int((hour*3600 + minute*60)*1000)
        treat = int(float(treat[:-1])*1000)
        temp.append((second-treat+1, second))

    # 끝나는 시간을 기준으로 정렬해준다.
    temp.sort(key=lambda x: x[1])

    # 끝나는 시간+1000이 시작시간보다 크게된다면 1초내에 같은 트래픽이 된다.
    for i in range(len(temp)):
        cnt = 1
        for j in range(i+1, len(temp)):
            if(temp[i][1]+1000 > temp[j][0]):
                cnt += 1
        answer = max(answer, cnt)

    return answer
