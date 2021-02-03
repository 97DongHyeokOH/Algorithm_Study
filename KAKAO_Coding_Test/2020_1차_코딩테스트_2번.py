# 1단계부터 반복하는 재귀 함수
def solution(p):
    if(not p):
        return ''

    answer = ''

    p1 = 0
    p2 = 0

    for idx in range(len(p)):
        if(p[idx] == '('):
            p1 += 1
        else:
            p2 += 1

        if(p1 == p2):
            u = p[:idx+1]
            v = p[idx+1:]
            break
        idx += 1

    if(correct(u)):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')' + rever(u)

    return answer

# 올바른 괄호 문자열 판단


def correct(u):
    stack = []

    for i in u:
        if(i == '('):
            stack.append(i)
        elif(i == ')' and stack and stack[len(stack)-1] == '('):
            stack.pop()
        else:
            return False

    return True

# 4-4 역할 수행


def rever(u):
    arr = list(u)
    arr.pop(0)
    arr.pop()

    temp = ''

    for i in arr:
        if(i == '('):
            temp += ')'
        else:
            temp += '('

    return temp
