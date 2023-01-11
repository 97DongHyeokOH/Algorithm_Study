import sys

input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))
st_num = int(input())

for _ in range(st_num):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(n):
            if (i+1) % num == 0:
                switch[i] = (switch[i]+1) % 2

    if sex == 2:
        switch[num-1] = (switch[num-1]+1) % 2
        k = 1

        while num - k - 1 >= 0 and num + k - 1 < n and switch[num-k-1] == switch[num+k-1]:
            switch[num-k-1] = (switch[num-k-1]+1) % 2
            switch[num+k-1] = (switch[num+k-1]+1) % 2
            k += 1

for i in range(n):
    if i and i % 20 == 0:
        print()
    print(switch[i], end=' ')
