def fac(num):
    t = 1
    for i in range(num):
        t *= (i+1)
    return t

def solution(n, k):
    answer = []
    
    q = []       
    for i in range(n):
        q.append(i+1)
    
    k = k - 1
    d = fac(n) // n
    c = 1
    while k > 0:
        a, k = k // d, k % d
        
        d = d // (n-c)
        
        c += 1
        
        answer.append(q.pop(a))
    
    for qq in q:
        answer.append(qq)
        
    return answer