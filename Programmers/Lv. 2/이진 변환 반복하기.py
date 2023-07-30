def solution(s):
    r = 0
    c = 0
    while s != '1':
        n = s.count('1')
        c += len(s) - n
        s = bin(n)[2:]        
        r += 1
        
    return [r, c]