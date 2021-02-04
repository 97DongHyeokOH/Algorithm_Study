from collections import deque as dq

# 한번 turn 할 때 마다 key box에서의 위치


def cases(k, a, b):
    case = []
    for i in range(4):
        t_temp = turn(k, i, a, b)
        t_temp.sort()
        case.append(t_temp)

    return case


def solution(key, lock):
    k = []  # key에서 1 넣기
    l = []  # lock에서 0 넣기
    # 가운데 lock box가 위치해 있고 그 주위에 key box만한 크기들이 둘러 쌓여있는 배열 생성을 위함
    a = len(key)
    b = len(lock)
    t = b + a*2

    for i in range(len(key)):
        for j in range(len(key)):
            if(key[i][j]):
                k.append((i, j))

    # 90도를 4번 회전한 case들을 추출
    case = cases(k, a, b)

    for i in range(b):
        for j in range(b):
            if(not lock[i][j]):
                l.append((i+len(key), j+len(key)))

    for i in range(t-a+1):
        for j in range(t-a+1):
            for k in case:
                temp = []
                for y, x in k:
                    if(pos(i+y, j+x, a, a+b)):
                        temp.append((i+y, j+x))
                temp.sort()
                if(temp == l):
                    return True

    return False

# n+1번 turn 했을때 key 박스에서의 위치


def turn(k, n, a, b):
    for _ in range(n+1):
        temp = []
        for y, x in k:
            temp.append((x, a-1-y))
        k = temp.copy()

    return temp

# 가운데에 있는 lock 박스 안쪽에 위치한지 확인하기 위함


def pos(y, x, a, b):
    if(a <= y < b and a <= x < b):
        return True
    return False
