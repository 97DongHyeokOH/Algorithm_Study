import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())

words_bit = []
# 꼭 배워야되는 알파벳
essential = {'a', 'c', 'i', 'n', 't'}
# 모든 단어들에서 나오는 알파벳 (essential은 제외)
alpha = set()
# 결과값
result = 0

for _ in range(n):
    # 입력받은 단어에서 essential은 빼준다.
    word = set(list(input().rstrip())) - essential

    # essential 단어를 제외하고 k-5개 보다 많은 단어는 절대 배우지 못하는 단어
    if(len(word) > k-5):
        continue

    # alpha 집합에 단어의 알파벳을 합집합으로 넣어준다.
    alpha = alpha.union(word)
    # 단어에 포함되는 알파벳은 비트로 표현
    bit = 0
    for c in word:
        bit |= (1 << ord(c)-97)
    words_bit.append(bit)

# k가 5보다 작으면 essential 단어도 못배우기 때문
# 배울수 있는 단어가 0개
if(k < 5 or not words_bit):
    print(0)
    exit(0)

# alpha 집합에 든 알파벳의 숫자와 최대로 배울수 있는 k-5중에 작은 수로 조합을 만들어준다.
for temp in list(combinations(alpha, min(len(alpha), k-5))):
    # 조합을 비트로 표현
    bit = 0
    # 현재 조합으로 만들 수 있는 단어의 수
    cnt = 0

    for c in temp:
        bit |= (1 << ord(c)-97)

    for wb in words_bit:
        # 현재 조합의 비트와 단어의 비트를 and연산해서 단어의 비트가 나오면 만들 수 있는 단어이다.
        if(bit & wb == wb):
            cnt += 1

    result = max(result, cnt)

print(result)
