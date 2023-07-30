def solution(weights):
    answer = 0
    
    temp = {}
    
    ratio = [1, 1/2, 2/3, 3/4, 3/2, 4/3, 2]
    for weight in weights:
        for r in ratio:
            if weight * r in temp.keys():
                answer += temp[weight * r]
        if weight not in temp.keys():
            temp[weight] = 1
        else:
            temp[weight] += 1
    
    return answer