# 나의 풀이
def solution(s):
    temp = s.replace('{', '').replace('}', '').split(',')
    temp_set = set(temp)

    arr = []

    for i in temp_set:
        cnt = temp.count(i)
        arr.append((cnt, int(i)))

    arr.sort(reverse=True)

    result = []

    for i in arr:
        result.append(i[1])

    return result

# 다른 사람들의 풀이
# import re -> 정규 표현식
# from collections import Counter

# def solution(s):
#     s = Counter(re.findall('\d+', s)) -> s에서 정수인것만 추출해서 Counter을 사용해 dict에 저장해줌
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
