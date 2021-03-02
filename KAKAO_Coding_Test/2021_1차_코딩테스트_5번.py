def solution(play_time, adv_time, logs):
    adv_t = adv_time.split(':')
    play_t = play_time.split(':')
    # 광고시간과 총 재생 시간을 초단위로 변경
    adv = int(adv_t[0])*3600 + int(adv_t[1])*60 + int(adv_t[2])
    play = int(play_t[0])*3600 + int(play_t[1])*60 + int(play_t[2])

    time = [0]*(play+1)
    start_arr = [0]*(play+1)
    end_arr = [0]*(play+1)

    # logs에 있는 값을 초 단위로 변환
    for log in logs:
        t = log.replace('-', ':').split(':')

        start = int(t[0])*3600 + int(t[1]) * 60 + int(t[2])
        end = int(t[3])*3600 + int(t[4]) * 60 + int(t[5])

        start_arr[start] += 1
        end_arr[end] += 1

    # idx-1 ~ idx까지 겹치는 시간 수
    time[0] = 0

    for idx in range(1, play+1):
        time[idx] = time[idx-1] + start_arr[idx-1] - end_arr[idx-1]

    # result는 idx-adv ~ idx까지 시간 최대 값, answer는 초단위로 결과 값 저장
    result = 0
    answer = 0

    # 0 ~ idx까지 시간을 합한 값
    for idx in range(1, len(time)):
        time[idx] = time[idx] + time[idx-1]

    for idx in range(adv, play+1):
        if(result < time[idx]-time[idx-adv]):
            result = time[idx]-time[idx-adv]
            answer = idx - adv

    # 결과 값을 HH:MM:SS로 변환
    result = ''

    t = []

    t.append(answer // 3600)
    t.append(answer % 3600 // 60)
    t.append(answer % 60)

    for i in t:
        if(i < 10):
            result += '0'
        result += str(i) + ':'

    return result.rstrip(':')
