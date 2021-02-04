# 내가 원래 푼 방법

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    rever = 0
    result = '['

    func = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()
    
    s = s.replace('[', '')
    s = s.replace(']', '')

    arr = s.split(',')

    front = 0
    back = len(arr)

    if(func.count('D') > n):
        print('error')
        continue

    for f in func:
        if(f == 'R'):
            rever = (rever + 1) % 2
        else:
            if(rever):
                back -= 1
            else:
                front += 1
    
    arr = arr[front:back]
    
    if(not arr):
        result = '[]'
    elif(rever):
        idx = len(arr)-1
        while(idx):
            result += arr[idx] + ','
            idx -= 1
        result += arr[idx] + ']'
    else:
        idx = 0
        while(idx < len(arr)-1):
            result += arr[idx] + ','
            idx += 1
        result += arr[idx] + ']'
    
    print(result)

# deque를 활용

# import sys
# from collections import deque

# t=int(sys.stdin.readline())
# for i in range(t):
#     cmd=sys.stdin.readline().rstrip()
#     n=int(sys.stdin.readline()) 
#     dq=sys.stdin.readline()

#     if(n==0): 
#         dq=deque()
#     else: 
#         dq=deque(list(map(int,dq[1:-2].split(','))))

#     isReverse = 0
#     left,right = 0,0

#     for p in cmd:
#         if(p=='R'):
#             isReverse = (isReverse + 1) % 2
#         else : #p=='D'
#             if dq:
#                 if(isReverse):
#                     dq.pop()
#                 else:
#                     dq.popleft()
#             else:
#                 print('error')
#                 break        
#     else:
#         if(isReverse):
#             dq=reversed(dq)
#         print("[" + ",".join(list(map(str, dq))) + "]")