import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 만약 모든 나무 길이의 합이 3의 배수가 안된다면 불가능하다. -> 하루에 총 3의 나무가 자라야되는데 3의 배수가 아니라면 불가능하다
if(sum(arr) % 3):
    print('NO')
else:
    # 2씩 자랄 수 있는 횟수가 모든 나무 길이의 합을 3으로 나눈 몫보다 크거나 같아야 한다 -> 그렇지 않으면 물을 뿌리다 보면 2만큼 나무가 자랄수 없는 경우가 존재
    cnt = 0

    for i in arr:
        cnt += i // 2
    
    if(cnt >= sum(arr) // 3):
        print('YES')
    else:
        print('NO')