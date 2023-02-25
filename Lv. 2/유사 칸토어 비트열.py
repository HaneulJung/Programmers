def convert(num):
    temp = [0, 1, 2, 2, 3]
    a = []
    while num > 0:        
        d = num % 5
        a.append(d)
        num = num // 5
    
    s = 0
    for i, aa in enumerate(reversed(a)):
        s += temp[aa] * (4 ** (len(a) - i - 1))
        if aa == 2:
            break
            
    return s
    

def solution(n, l, r):  
    return convert(r) - convert(l-1)