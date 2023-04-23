from math import gcd

def solution(arrayA, arrayB):
    l = len(arrayA)
    
    for i in range(l):
        if i == 0:
            gcd_A = arrayA[i]
        else:
            gcd_A = gcd(gcd_A, arrayA[i])
        
        if gcd_A == 1:
            break
    
    for i in range(l):
        if i == 0:
            gcd_B = arrayB[i]
        else:
            gcd_B = gcd(gcd_B, arrayB[i])
        
        if gcd_B == 1:
            break
    
    if gcd_A != 1:
        for B in arrayB:
            if B % gcd_A == 0:
                gcd_A = 0
                break
    else:
        gcd_A = 0
                
    if gcd_B != 1:
        for A in arrayA:
            if A % gcd_B == 0:
                gcd_B = 0
                break
    else:
        gcd_B = 0
    
    return max(gcd_A, gcd_B)