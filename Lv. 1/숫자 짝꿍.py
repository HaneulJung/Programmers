def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        s = str(i)
        answer += str(s * min(X.count(s), Y.count(s)))
    
    if answer == '':
        return '-1'
    elif answer[0] == '0':
        return '0'
    
    return answer