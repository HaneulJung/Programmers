import math

def solution(n):
    m = math.sqrt(n)
    if m - int(m) == 0:
        return 1
    else:
        return 2