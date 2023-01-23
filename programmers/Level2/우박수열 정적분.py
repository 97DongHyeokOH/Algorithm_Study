def solution(k, ranges):
    answer = []
    temp = [(0, k)]
    area = []
    i = 1

    while k > 1:
        if k % 2:
            k = k*3 + 1
        else:
            k //= 2

        temp.append((i, k))
        i += 1

    for i in range(len(temp)-1):
        x, y = temp[i]
        nx, ny = temp[i+1]

        area.append(max(y, ny) - abs(y - ny) * 0.5)

    for start, end in ranges:
        if len(area)+end < start:
            answer.append(-1)
        else:
            answer.append(sum(area[start:len(area)+end]))

    return answer


print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))
