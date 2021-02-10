from collections import deque as dq


def solution(begin, target, words):
    q = dq([(begin, 0)])
    visit = [False]*len(words)

    while(q):
        word, cnt = q.popleft()

        if(word == target):
            return cnt

        for idx in range(len(words)):
            if(not visit[idx] and compare(word, words[idx])):
                q.append((words[idx], cnt+1))
                visit[idx] = True

    return 0


def compare(w1, w2):
    cnt = 0
    for a, b in zip(w1, w2):
        if(a != b):
            cnt += 1

    if(cnt == 1):
        return True
    return False


print(solution())
