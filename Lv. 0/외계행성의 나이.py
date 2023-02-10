def solution(age):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    answer = ''
    for a in str(age):
        answer += alpha[int(a)]    
    return answer