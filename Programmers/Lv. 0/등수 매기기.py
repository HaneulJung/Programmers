def solution(score):
    answer = []
    
    sum_list = []
    
    for s in score:
        sum_list.append(sum(s))
    
    for sl in sum_list:
        answer.append(sorted(sum_list, reverse=True).index(sl)+1)
    
    return answer