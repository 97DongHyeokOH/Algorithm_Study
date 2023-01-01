import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

rome_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
            'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

num1 = 0
num2 = 0
num_result = 0
rome_result = ''

for i in range(len(s1)):
    if i and temp > 0:
        if temp < rome_num[s1[i]]:
            num1 += rome_num[s1[i]] - temp
            temp = -1
        else:
            num1 += temp
            temp = rome_num[s1[i]]
    else:
        temp = rome_num[s1[i]]

if temp > 0:
    num1 += temp

for i in range(len(s2)):
    if i and temp > 0:
        if temp < rome_num[s2[i]]:
            num2 += rome_num[s2[i]] - temp
            temp = -1
        else:
            num2 += temp
            temp = rome_num[s2[i]]
    else:
        temp = rome_num[s2[i]]

if temp > 0:
    num2 += temp

num_result = num1+num2

print(num_result)

for k, v in sorted(rome_num.items(), reverse=True, key=lambda x: x[1]):
    if num_result == 0:
        break

    while(num_result >= v):
        rome_result += k
        num_result -= v

print(rome_result)
