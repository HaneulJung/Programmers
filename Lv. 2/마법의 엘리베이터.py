def solution(storey):
    answer = 0
    
    while storey > 0:
        storey, mod = storey // 10, storey % 10
        
        if mod < 5:
            answer += mod
        elif mod > 5:
            answer += (10 - mod)
            storey += 1
        else:
            answer += 5
            if storey % 10 >= 5:
                storey += 1
    
    return answer