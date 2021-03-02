def solution(play_time, adv_time, logs):
    adv_t = adv_time.split(':')
    play_t = play_time.split(':')
    # 광고시간과 총 재생 시간을 초단위로 변경
    adv = int(adv_t[0])*3600 + int(adv_t[1])*60 + int(adv_t[2])
    play = int(play_t[0])*3600 + int(play_t[1])*60 + int(play_t[2])

    time = [0]*(play+1)
    start_arr = [0]*(play+1)
    end_arr = [0]*(play+1)

    for log in logs:
        t = log.replace('-', ':').split(':')

        start = int(t[0])*3600 + int(t[1]) * 60 + int(t[2])
        end = int(t[3])*3600 + int(t[4]) * 60 + int(t[5])

        start_arr[start] += 1
        end_arr[end] += 1

    time[0] = 0

    for idx in range(1, play+1):
        time[idx] = time[idx-1] + start_arr[idx-1] - end_arr[idx-1]

    temp = 0
    result = 0
    answer = 0

    for idx in range(1, len(time)):
        time[idx] = time[idx] + time[idx-1]

    for idx in range(adv, play+1):
        if(result < time[idx]-time[idx-adv]):
            result = time[idx]-time[idx-adv]
            answer = idx - adv

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


a = "02:03:55"
b = "00:14:15"
c = ["01:20:15-01:45:14", "00:40:31-01:00:00",
     "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(a, b, c))
