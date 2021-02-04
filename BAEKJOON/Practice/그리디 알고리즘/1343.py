def fill(temp):
    n = len(temp)

    a = n // 4
    n %= 4
    b = n // 2
    n %= 2

    if(n):
        return -1, -1
    
    return a, b

p = input()

result = ''
temp = ''

for i in p:
    if(i == '.'):
        a, b = fill(temp)
        temp = ''

        if(a == -1):
            result = '-1'
            break

        result += ('AAAA' * a + 'BB' * b)
        result += i
    else:
        temp += i

a, b = fill(temp)

result += ('AAAA' * a + 'BB' * b)

if(a == -1):
    result = '-1'

print(result)