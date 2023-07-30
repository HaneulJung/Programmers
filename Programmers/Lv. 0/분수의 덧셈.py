import math

def solution(numer1, denom1, numer2, denom2):    
    num = numer1 * denom2 + numer2 * denom1
    den = denom1 * denom2
    
    g = math.gcd(num, den)
    
    return [num / g, den / g]