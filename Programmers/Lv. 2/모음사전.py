def solution(word):
    dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    
    t = [781, 156, 31, 6, 1]
    
    answer = 0
    
    for i, w in enumerate(word):
        answer += dic[w] * t[i]
    
    
    return answer + len(word)