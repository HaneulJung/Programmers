def fac(num):
    a = 1
    for i in range(1, num+1):
        a *= i
    return a

def solution(balls, share):
                
    return fac(balls) / (fac(balls-share) * fac(share))