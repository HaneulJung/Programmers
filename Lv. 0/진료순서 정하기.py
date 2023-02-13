def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse=True)
    for t in emergency:
        answer.append(temp.index(t)+1)
        
    return answer