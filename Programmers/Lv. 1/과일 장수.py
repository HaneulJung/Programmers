def solution(k, m, score):
    answer = 0
    s = sorted(score, reverse=True)
    for i in range(0,len(s),m):
        if i + m <= len(s):
            answer += s[i+m-1] * m
    return answer