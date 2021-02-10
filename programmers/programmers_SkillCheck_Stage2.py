from itertools import permutations


def solution1(str1, str2):
    answer = 0
    arr1 = []
    arr2 = []
    temp = ''
    inter = 0

    for c in str1:
        if('A' <= c.upper() <= 'Z'):
            temp += c.upper()

            if(len(temp) == 2):
                arr1.append(temp)
                temp = c.upper()
        else:
            temp = ''

    temp = ''

    for c in str2:
        if('A' <= c.upper() <= 'Z'):
            temp += c.upper()

            if(len(temp) == 2):
                arr2.append([temp, 0])
                temp = c.upper()
        else:
            temp = ''

    if(not arr1 and not arr2):
        return 65536

    for i in arr1:
        for j in arr2:
            if(i == j[0] and not j[1]):
                j[1] = 1
                inter += 1
                break

    answer = inter / (len(arr1)+len(arr2)-inter)

    return int(answer*65536)


def solution2(numbers):
    answer = 0
    number = set()
    for i in range(1, len(numbers)+1):
        p = list(permutations(numbers, i))
        for j in p:
            idx = 0
            num = 0
            while(idx < i):
                num *= 10
                num += int(j[idx])
                idx += 1
            number.add(num)

    for n in number:
        if(is_prime(n)):
            answer += 1

    return answer


def is_prime(num):
    if(num <= 1):
        return False

    for i in range(2, int(num**0.5) + 1):
        if(num % i == 0):
            return False
    return True


print(solution('011'))
