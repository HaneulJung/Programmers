def solution(n, numlist):
    answer = []
    
    for l in numlist:
        if (l % n == 0):
            answer.append(l)
    
    return answer