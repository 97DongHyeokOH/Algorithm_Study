s = input()

zeroCnt = 0
oneCnt = 0

if(s[0] == '0'):
    isZero = True
    isOne = False
    zeroCnt += 1
else:
    isZero = False
    isOne = True
    oneCnt += 1

for num in s:
    if(isZero and num == '1'):
        isZero = False
        isOne = True
        oneCnt += 1
    elif(isOne and num == '0'):
        isZero = True
        isOne = False
        zeroCnt += 1