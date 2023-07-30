def solution(dots):
    
    odd = [[(0,1), (2,3)], [(0,2), (1,3)], [(0,3), (1,2)]]
    
    for o in odd:
        a1 = o[0][0]
        a2 = o[0][1]
        a3 = o[1][0]
        a4 = o[1][1]
        
        if (dots[a1][1] - dots[a2][1]) / (dots[a1][0] - dots[a2][0]) \
            == (dots[a3][1] - dots[a4][1]) / (dots[a3][0] - dots[a4][0]):
            return 1
        
    return 0
        
    