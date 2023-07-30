def solution(array):    
    s = ""    
    for a in array:
        s += str(a)
    
    return s.count("7")