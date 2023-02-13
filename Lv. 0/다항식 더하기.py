def solution(polynomial):
    x, num = 0, 0
    
    for p in polynomial.split(" + "):
        if 'x' in p:
            if 'x' == p:
                x += 1
            else:
                x += int(p[0])
        else:
            num += int(p)
    
    answer = ''
    
    if x == 0:
        if num == 0:
            return '0'
        else:
            return str(num)
    elif x == 1:
        answer += 'x'
    else:
        answer += str(x) + 'x'
    
    if num == 0:
        return answer
    else:
        return answer + ' + ' + str(num)
        
                