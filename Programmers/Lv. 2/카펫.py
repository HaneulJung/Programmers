def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    
    for i in range(1, yellow):
        if yellow % i == 0:
            if (i + 2) * (yellow / i + 2) == brown + yellow:
                return [yellow / i + 2, i + 2]