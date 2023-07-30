def solution(cipher, code):
    answer = ''
    
    l = list(cipher)
    
    for i in range(1, len(l)+1):
        if (i % code == 0):
            answer += l[i-1]
    
    return answer