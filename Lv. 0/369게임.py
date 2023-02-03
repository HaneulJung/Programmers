def solution(order):
    s = str(order) 
    
    return s.count("3") + s.count("6") + s.count("9")