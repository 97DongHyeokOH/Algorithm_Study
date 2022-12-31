import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def make_all_clock_num(n1, n2, n3, n4):
    if visit[int(n1)][int(n2)][int(n3)][int(n4)] or int(n1) > 9 or int(n2) > 9 or int(n3) > 9 or int(n4) > 9:
        return

    visit[int(n1)][int(n2)][int(n3)][int(n4)] = True
    min_num = min(int(n1+n2+n3+n4), int(n2+n3+n4+n1),
                  int(n3+n4+n1+n2), int(n4+n1+n2+n3))
    clock_num.add(min_num)

    make_all_clock_num(str(int(n1)+1), n2, n3, n4)
    make_all_clock_num(n1, str(int(n2)+1), n3, n4)
    make_all_clock_num(n1, n2, str(int(n3)+1), n4)
    make_all_clock_num(n1, n2, n3, str(int(n4)+1))


clock_num = set()
visit = [[[[False]*11 for _ in range(11)]
          for _ in range(11)] for _ in range(11)]

make_all_clock_num('1', '1', '1', '1')

clock_num = sorted(list(clock_num))

n1, n2, n3, n4 = input().rstrip().split()

cur_num = min(int(n1+n2+n3+n4), int(n2+n3+n4+n1),
              int(n3+n4+n1+n2), int(n4+n1+n2+n3))

print(clock_num.index(cur_num)+1)
