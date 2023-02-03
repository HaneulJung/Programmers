def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer


#%% 
def bin2dec(n):
    result = 0
    s = str(n)
    l = len(s)
    c = 0
    
    for i in range(l-1, -1, -1):
        result += int(s[i]) * (2 ** c)
        c += 1
    return result
    
def dec2bin(n):
    s = []
    if (n==0):
        return "0"
    while n // 2 != 0:
        d = n % 2
        n = n // 2        
        s.append(d)
    s.append(1)
    
    r = ''
    for i in range(len(s)-1, -1, -1):
        r += str(s[i])
        
    return r

def solution(bin1, bin2):
    return str(dec2bin(bin2dec(bin1) + bin2dec(bin2)))
    