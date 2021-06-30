# 문제: 옛날에 백은진이라는 마법사가 S개의 마법의 구슬을 만들었다. 이 마법의 구슬은 함께 모여있을 때는, 상상을 초월하는 힘의 근원이 된다. 이것을 김지민과 같은 악당이 사용하는 것을 막기 위해 백은진은 F개의 가짜 구슬을 만들었다. 이 가짜 구슬은 마법의 구슬과 똑같이 생겼지만, 마법의 힘은 없다.
# 이제 김형택은 세계를 지배하기 위해 어떤 구슬이 진짜 구슬인지 알아야 한다. 따라서 김지민은 N명의 사람을 모아서, S+F개 중 모든 S개의 조합을 테스트하기로 했다.
# 김형택은 각 사람들에게 미리 어떤 조합을 테스트 할 것인지 정해주었다. 그리고 같은 조합을 최대 한 번만 테스트한다.
# 그런데, 이 사람들은 절대로 다른 사람보다 일을 많이 하지 않는다. 즉, 모두 같은 개수의 조합을 테스트 한다. 따라서 김형택은 몇 명의 사람을 뽑아야, 모든 조합을 테스트하면서, 모든 사람이 같은 횟수의 테스트를 하는지 궁금해졌다.
# 김형택이 모을 수 있는 사람의 최댓값 M이 주어질 때, M을 넘지 않으면서, 김형택이 뽑을 수 있는 최대 사람의 수를 구하는 프로그램을 작성하시오

# 입력: 첫째 줄에 S F M이 주어진다. S와 F는 1,000,000,000보다 작거나 같은 자연수이고, M은 100,000보다 작거나 같은 자연수이다.

# 출력: 첫째 줄에 문제의 정답을 출력한다. 만약 불가능 할 때는 -1을 출력한다.

import sys

# 팩토리얼을 소인수 분해


def prime_fact(n):
    prime_fact_arr = [0]*(m+1)

    for i in primes:
        if(i > n):
            return prime_fact_arr

        result = 0
        temp = i
        while(temp <= n):
            result += n // temp
            temp *= i
        prime_fact_arr[i] = result

    return prime_fact_arr

# 그냥 자연수를 소인수 분해


def prime_fact2(n):
    prime_fact_arr = [0]*(m+1)

    for i in primes:
        if(i > n):
            return prime_fact_arr

        k = 0

        while(n % i == 0):
            n //= i
            k += 1

        prime_fact_arr[i] = k

    return prime_fact_arr


s, f, m = map(int, sys.stdin.readline().split())

num = [False, False] + [True]*(m-1)
primes = []
ans = 0

for i in range(2, m+1):
    if(num[i]):
        primes.append(i)
        for j in range(i+i, m+1, i):
            num[j] = False

prime_fact_denominator = prime_fact(s+f)
prime_fact_numerator_1 = prime_fact(s)
prime_fact_numerator_2 = prime_fact(f)

result_prime_fact = [0]*(m+1)

for i in range(2, m+1):
    result_prime_fact[i] = prime_fact_denominator[i] - \
        prime_fact_numerator_1[i] - prime_fact_numerator_2[i]

for i in range(m, 0, -1):
    prime_f = prime_fact2(i)

    for idx in primes:
        if(result_prime_fact[idx] < prime_f[idx]):
            break

        if(idx == primes[len(primes)-1]):
            ans = i

    if(ans):
        print(ans)
        break
