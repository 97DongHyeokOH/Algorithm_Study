def solution(routes):
    answer = 0

    routes.sort(key=lambda x: (x[0], -x[1]))

    prev_end = routes[0][1]

    for start, end in routes[1:]:
        if prev_end < start:
            answer += 1
            prev_end = end
        else:
            prev_end = min(prev_end, end)

    return answer + 1
