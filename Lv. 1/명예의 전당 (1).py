def solution(k, score):
    answer = [score[0]]
    for i in range(1,len(score)):
        if i < k:
            answer.append(min(score[:i+1]))
        else:
            answer.append(sorted(score[:i+1], reverse=True)[k-1])
    return answer