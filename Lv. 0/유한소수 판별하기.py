def gcd(a, b):
    for i in range(min(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            return i
        
def solution(a, b):
    g = gcd(a, b) 
    
    b = b // g
    
    if b in [1, 2, 5]:
        return 1
    else:
        while b % 2 == 0:
            b = b // 2
        while b % 5 == 0:
            b = b // 5
        if b == 1:
            return 1
        else:
            return 2