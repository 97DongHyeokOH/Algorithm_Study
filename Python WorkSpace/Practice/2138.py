import sys

n = int(sys.stdin.readline().rstrip('\n'))

before = list(sys.stdin.readline().rstrip('\n'))
after = list(sys.stdin.readline().rstrip('\n'))

temp = before.copy()

cnt1 = 0
cnt2 = 1

for idx in range(1, n):
    if(temp[idx-1] != after[idx-1]):
        if(temp[idx-1] == '0'):
            temp[idx-1] = '1'
        else:
            temp[idx-1] = '0'
        
        if(temp[idx] == '0'):
            temp[idx] = '1'
        else:
            temp[idx] = '0'
        
        if(idx+1 != n):
            if(temp[idx+1] == '0'):
                temp[idx+1] = '1'
            else:
                temp[idx+1] = '0'
        
        cnt1 += 1

if(temp != after):
    cnt1 = -1

temp = before.copy()
if(temp[0] == '0'):
    temp[0] = '1'
else:
    temp[0] = '0'

if(temp[1] == '0'):
    temp[1] = '1'
else:
    temp[1] = '0'

for idx in range(1, n):
    if(temp[idx-1] != after[idx-1]):
        if(temp[idx-1] == '0'):
            temp[idx-1] = '1'
        else:
            temp[idx-1] = '0'
        
        if(temp[idx] == '0'):
            temp[idx] = '1'
        else:
            temp[idx] = '0'
        
        if(idx+1 != n):
            if(temp[idx+1] == '0'):
                temp[idx+1] = '1'
            else:
                temp[idx+1] = '0'
        
        cnt2 += 1

if(temp != after):
    cnt2 = -1

if(cnt1 >= 0 and cnt2 >= 0):
    print(min(cnt1, cnt2))
elif(cnt1 < 0 and cnt2 < 0):
    print(-1)
else:
    print(max(cnt1, cnt2))