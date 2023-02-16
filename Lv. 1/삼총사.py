from itertools import combinations

def solution(number):
    answer = 0
    
    for l in combinations(number, 3):
        if sum(l) == 0:
            answer += 1
    
    return answer