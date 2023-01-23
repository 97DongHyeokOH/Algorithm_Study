def solution(storey):
    answer = float("inf")
    str_storey_reversed = str(storey)[::-1]
    
    storey_list = [int(i) for i in str_storey_reversed]
    
    def get_answer(i, add1, cur):
        nonlocal answer
        
        if i == len(str_storey_reversed):
            if add1:
                cur += 1
            answer = min(answer, cur)
            return
        
        cur_num = storey_list[i]
        
        if add1:
            cur_num += 1
        
        get_answer(i+1, True, cur + 10 - cur_num)
        get_answer(i+1, False, cur + cur_num)
        
    get_answer(0, False, 0)

    return answer