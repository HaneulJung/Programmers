def solution(numbers):    
    n = sorted(numbers, reverse=True)
    return n[0] * n[1]