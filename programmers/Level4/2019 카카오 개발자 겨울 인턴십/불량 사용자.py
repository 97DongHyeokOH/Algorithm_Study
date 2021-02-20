from itertools import permutations


def solution(user_id, banned_id):
    result = []
    perm = permutations(user_id, len(banned_id))

    def compare(s1, s2):
        if(len(s1) != len(s2)):
            return False

        for c1, c2 in zip(s1, s2):
            if(c2 != '*' and c1 != c2):
                return False
        return True

    for l in list(perm):
        k = list(l)
        check = 0

        for idx in range(len(l)):
            if(not compare(k[idx], banned_id[idx])):
                check = 1
                break

        if(not check):
            k.sort()
            if(k not in result):
                result.append(k)

    return len(result)
