def convertN(num, n):
    l = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    if num == 0:
        return '0'
    
    temp = ''
    while num != 0:
        if num % n >= 10:
            temp += l[num % n]
        else:
            temp += str(num % n)
        num //= n
    return temp[::-1]

def solution(n, t, m, p):
    answer = ''
    
    temp = ''
    num = 0
    i = p - 1
    while i < m * t:
        if i > len(temp) - 1:
            temp += convertN(num, n)
            num += 1
        else:
            answer += temp[i]
            i += m
    
    return answer