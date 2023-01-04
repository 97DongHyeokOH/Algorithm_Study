import sys

input = sys.stdin.readline

s = input().rstrip()
result = ''
bracket_on = False
temp = ''

for c in s:
    if c == '<':
        if temp:
            result += temp[::-1]
            temp = ''
        bracket_on = True
        temp += c
    elif c == '>':
        bracket_on = False
        temp += c
        result += temp
        temp = ''
    elif c == ' ':
        if bracket_on:
            temp += c
        else:
            result += temp[::-1] + ' '
            temp = ''
    else:
        temp += c

print(result + temp)
