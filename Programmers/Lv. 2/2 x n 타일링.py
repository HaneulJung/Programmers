def solution(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        pre1 = 1
        pre0 = 2
        for _ in range(n-2):
            cur = pre0 + pre1
            pre1 = pre0
            pre0 = cur
        
    
    return cur % 1000000007

def solution(n):
    
    a, b = 1, 1
    
    for _ in range(n):
        a, b = b, (a+b)           
    
    return a % 1000000007