def solution(clothes):    
    dict = {}
    
    for cloth in clothes:
        if cloth[1] not in list(dict.keys()):
            dict[cloth[1]] = 1
        else:
            dict[cloth[1]] += 1
    
    answer = 1
    for type in dict:
        answer *= (dict[type] + 1)
    
    return answer-1