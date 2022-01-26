import sys

input = sys.stdin.readline

# 유니온(Union) 함수 -> 사전순으로 앞에오는 이름을 부모로 합쳐준다.


def Union(x, y):
    a = Find(x)
    b = Find(y)

    if(a != b):
        network[a][1] += network[b][1]
        network[b][1] = network[a][1]

    network[max(a, b)][0] = min(a, b)

# 파인드(Find) 함수


def Find(x):
    if(x == network[x][0]):
        return network[x][0]
    else:
        network[x][0] = Find(network[x][0])
        return network[x][0]


t = int(input())

for _ in range(t):
    f = int(input())

    # 네트워크를 표시해주는 딕셔너리 -> 부모로 연결되어있는 이름과 자신과 root에는 총 연결되어있는 친구의 수가 저장
    network = dict()

    for _ in range(f):
        a, b = input().rstrip().split()

        if(not a in network):
            network[a] = [a, 1]

        if(not b in network):
            network[b] = [b, 1]

        Union(a, b)
        # root에서만 친구 네트워크의 수를 정확히 판별
        root = Find(a)
        print(network[root][1])
