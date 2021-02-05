def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        cnt = 1
        temp = s[:i]
        idx = i
        result = ''
        while(idx+i <= len(s)):
            if(temp == s[idx:idx+i]):
                cnt += 1
            else:
                if(cnt != 1):
                    result += str(cnt)
                result += temp
                temp = s[idx:idx+i]
                cnt = 1
            idx += i
        if(cnt != 1):
            result += str(cnt)
        result += temp
        if(idx < len(s)):
            result += s[idx:]
        answer = min(answer, len(result))

    return answer
