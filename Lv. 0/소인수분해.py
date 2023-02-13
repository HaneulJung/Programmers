def solution(n):
    answer = []
    
    idx = 2
    while n > 1:
        if n % idx == 0:
            n = n / idx
            if idx not in answer:
                answer.append(idx)
            idx = 2
        else:
            idx += 1
    
    return answer