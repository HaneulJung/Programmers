def solution(k, tangerine):
    dic = {}
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
            
    dic = sorted(dic.values(), key=lambda x: x, reverse=True)
    
    s = 0
    c = 0
    for d in dic:
        s += d
        c += 1
        if s >= k:
            return c